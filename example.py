# emeraldai/dashboard/pages/analysis_modules/events_table.py
# pyright: standard

import logging
from dash.exceptions import PreventUpdate
from datetime import UTC, datetime, timedelta

import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Input, Output, State, callback, dcc, html
from sqlalchemy import Select

from emeraldai.dashboard.pages.analysis_modules.chart_utils import COLOR_PALETTE
from emeraldai.dashboard.pages.analysis_modules.data_transforms import (
    EventTableDataEntry,
    format_table_data,
    job_ids_in_time_window,
    power_targets_in_time_window,
)
from emeraldai.dashboard.pages.analysis_modules.store import AnalysisWindowData
from emeraldai.db.connection import readonly_session_factory
from emeraldai.db.models import PowerTarget
from emeraldai.dashboard.styles import get_interval_options_for_role

from emeraldai.dashboard.auth import is_admin

# When the user selects an event, how much extra time to include around it
EVENT_SELECTION_BUFFER = timedelta(minutes=10)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def user_datetime_str(dt: datetime) -> str:
    """Formats a datetime object into a user-friendly but ISO-parseable string."""
    return dt.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


@callback(
    Output("signal-timeline-container", "children"),
    Input("url", "pathname"),
    State("theme-store", "data"),
)
def update_signal_table(_pathname: str, is_dark: bool) -> dbc.Alert | html.Div:
    """Populates the DR events table with filtering and sorting capabilities."""

    # Create the interactive data table
    data_table = dash.dash_table.DataTable(
        id="dr-events-table",
        columns=[
            {"name": "ID", "id": "id", "type": "numeric"},
            {"name": "Description", "id": "description", "type": "text"},
            {"name": "Date", "id": "date", "type": "text"},
            {"name": "Time", "id": "time", "type": "text"},
            {"name": "Duration", "id": "duration", "type": "text"},
            {"name": "Power Target (W)", "id": "power_target", "type": "text"},
            # Include raw columns for sorting/filtering but don't display them
            {"name": "_start_ts", "id": "_start_ts", "type": "numeric"},
            {"name": "_end_ts", "id": "_end_ts", "type": "numeric"},
        ],
        # Hide the columns with raw values using the style_cell_conditional property
        style_cell_conditional=[
            {
                "if": {"column_id": col},
                "display": "none",
            }
            for col in [
                "_start_ts",
                "_end_ts",
            ]
        ],  # type: ignore
        sort_action="native",
        sort_mode="single",
        filter_action="none",
        row_selectable="multi",  # Changed from "single" to "multi"
        selected_rows=[],
        style_table={"overflowX": "auto"},
        style_cell={
            "textAlign": "left",
            "padding": "8px",
            "fontSize": "14px",
        },
        style_header={
            "backgroundColor": "#2c3e50" if is_dark else "#f8f9fa",
            "color": "white" if is_dark else "black",
            "fontWeight": "bold",
            "textAlign": "left",
            "padding": "12px 8px",
        },
        page_size=10,
    )

    timeline_container = html.Div(
        [
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Label("Date Range:", size="sm"),
                                    dcc.DatePickerRange(
                                        id="dr-date-filter",
                                        start_date_placeholder_text="Start Date",
                                        end_date_placeholder_text="End Date",
                                        clearable=True,
                                        className="mb-2 w-100",
                                    ),
                                ],
                                width=12,
                            ),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Label("Min Duration (mins):", size="sm"),
                                    dbc.Input(
                                        id="dr-duration-filter",
                                        type="number",
                                        min=0,
                                        placeholder="Min duration",
                                        className="mb-2",
                                        debounce=True,
                                    ),
                                ],
                                width=4,
                            ),
                            dbc.Col(
                                [
                                    dbc.Label("Power Target (W):", size="sm"),
                                    dbc.Input(
                                        id="dr-power-filter",
                                        type="number",
                                        min=0,
                                        placeholder="power target",
                                        className="mb-2",
                                        debounce=True,
                                    ),
                                ],
                                width=4,
                            ),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Button(
                                        [
                                            html.I(className="fas fa-sync-alt me-2"),
                                            "Reset Filters",
                                        ],
                                        id="reset-filters-button",
                                        color="secondary",
                                        size="sm",
                                        className="mb-3 mt-1",
                                    ),
                                ],
                                className="d-flex justify-content-between w-100",
                                width=12,
                            ),
                        ]
                    ),
                ],
                className=f"mb-3 p-3 border rounded{' d-none' if not is_admin() else ''}",
            ),
            html.Span(
                "Select the events you wish to include. You only need to select the earliest and latest. You can also edit the times below."
            ),
            data_table,
            dbc.Card(
                dbc.CardBody(
                    dbc.Row(
                        [
                            # Start/End inputs in their own card
                            dbc.Col(
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            dbc.Label("Analysis Start (ISO):"),
                                            dcc.Input(
                                                id="analysis-start-input",
                                                className="w-150 mb-3 ms-2",
                                                value=user_datetime_str(
                                                    datetime.now(UTC)
                                                ),
                                            ),
                                            dbc.Label("Analysis End (ISO):"),
                                            dcc.Input(
                                                id="analysis-end-input",
                                                className="w-150 ms-3",
                                                value=user_datetime_str(
                                                    datetime.now(UTC)
                                                ),
                                            ),
                                        ]
                                    ),
                                    className="h-100",
                                ),
                                width=5,
                            ),
                            # Analyze button + dropdown + copy link in their own card
                            dbc.Col(
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            dbc.ButtonGroup(
                                                [
                                                    dbc.Button(
                                                        "Analyze Now",
                                                        id="analyze-now-button",
                                                        color="primary",
                                                        size="sm",
                                                        className="flex-grow-1",
                                                        n_clicks=0,
                                                    ),
                                                    dbc.Button(
                                                        [
                                                            html.I(className="fas fa-link me-1"),
                                                            "Copy Link",
                                                        ],
                                                        id="copy-link-button",
                                                        color="secondary",
                                                        outline=True,
                                                        size="sm",
                                                        style={"display": "none"},  # Hidden by default
                                                    ),
                                                ],
                                                id="button-group-container",
                                                className="w-100 mb-2",
                                            ),
                                            dbc.Tooltip(
                                                "Link copied!",
                                                target="copy-link-button",
                                                id="copy-link-tooltip",
                                                is_open=False,
                                                trigger="manual",
                                            ),
                                            dcc.Dropdown(
                                                id="data-resolution-dropdown",
                                                options=get_interval_options_for_role(is_admin()),  # pyright: ignore[reportArgumentType]
                                                placeholder="Select chart data resolution",
                                                value=None,
                                                className="w-100",
                                            ),
                                        ]
                                    ),
                                    className="h-100",
                                ),
                                width=4,
                            ),
                        ]
                    )
                ),
                className="mt-3",
            ),
        ]
    )

    return timeline_container


@callback(
    Output("analysis-start-input", "value", allow_duplicate=True),
    Output("analysis-end-input", "value", allow_duplicate=True),
    Input("dr-events-table", "selected_rows"),
    State("dr-events-table", "data"),
    prevent_initial_call=True,
)
def events_selected(
    selected_rows: list[int], table_data: list[EventTableDataEntry]
) -> tuple[str, str]:
    """Store the selected DR event IDs for later use."""
    if not selected_rows or not table_data:
        raise PreventUpdate

    start = end = None

    for row_idx in selected_rows:
        row = table_data[row_idx]
        row_start = datetime.fromtimestamp(row["_start_ts"], UTC)
        row_end = datetime.fromtimestamp(row["_end_ts"], UTC)
        if start is None or end is None:
            start = row_start
            end = row_end
        else:
            start = min(start, row_start)
            end = max(end, row_end)

    if start is None or end is None:
        raise PreventUpdate

    start -= EVENT_SELECTION_BUFFER
    end += EVENT_SELECTION_BUFFER

    return user_datetime_str(start), user_datetime_str(end)


@callback(
    Output("copy-link-button", "style"),
    Input("dr-events-table", "selected_rows"),
)
def toggle_copy_link_button(selected_rows: list[int] | None) -> dict:
    """Show Copy Link button only when 2+ events are selected to define a range."""
    if selected_rows and len(selected_rows) >= 2:
        return {"display": "inline-block"}  # Show button
    return {"display": "none"}  # Hide button


@callback(
    Output("analysis-window", "data"),
    Input("url", "search"),
    prevent_initial_call=False,
)
def load_analysis_from_query_string(
    search: str,
) -> AnalysisWindowData | None:
    """Load analysis window from URL query string parameters."""
    if not search:
        raise dash.exceptions.PreventUpdate

    # Parse query string (?start=...&end=...)
    from urllib.parse import parse_qs
    params = parse_qs(search.lstrip("?"))
    start_str = params.get("start", [None])[0]
    end_str = params.get("end", [None])[0]

    if start_str and end_str:
        # TODO: Add timestamp validation here
        logger.info(f"Loading analysis from query string: {start_str} - {end_str}")
        return {"start": start_str, "end": end_str}

    raise dash.exceptions.PreventUpdate


@callback(
    Output("analysis-start-input", "value", allow_duplicate=True),
    Output("analysis-end-input", "value", allow_duplicate=True),
    Input("analysis-window", "data"),
    prevent_initial_call=True,
)
def update_inputs_from_store(window_data: AnalysisWindowData | None) -> tuple[str, str]:
    """Update input fields when analysis window is set from query string or other sources."""
    if not window_data:
        raise dash.exceptions.PreventUpdate
    return window_data["start"], window_data["end"]


@callback(
    Output("analysis-window", "data", allow_duplicate=True),
    Input("analyze-now-button", "n_clicks"),
    State("analysis-start-input", "value"),
    State("analysis-end-input", "value"),
    prevent_initial_call=True,
)
def update_analysis_window(
    n_clicks: int, start_str: str, end_str: str
) -> AnalysisWindowData:
    """Updates the analysis window based on user input."""
    if n_clicks == 0:
        raise dash.exceptions.PreventUpdate
    # TODO: maybe do some validation on the datetime strings here
    # TODO: maybe add some automatic buffer time on the ends? seems annoying
    # to override what the user asked for. Instead, maybe add buffer when
    # selecting events.
    logger.info(f"Setting analysis window to {start_str} - {end_str}")
    return {"start": start_str, "end": end_str}


@callback(
    Output("dr-date-filter", "start_date"),
    Output("dr-date-filter", "end_date"),
    Output("dr-duration-filter", "value"),
    Output("dr-power-filter", "value"),
    Input("reset-filters-button", "n_clicks"),
)
def reset_filters(
    _n_clicks: int,
) -> tuple[datetime | None, datetime | None, None, None]:
    """Resets all filter inputs to their default state."""
    return datetime.now(UTC) - timedelta(days=7), None, None, None


@callback(
    Output("dr-events-table", "data"),
    Input("dr-date-filter", "start_date"),
    Input("dr-date-filter", "end_date"),
    Input("dr-duration-filter", "value"),
    Input("dr-power-filter", "value"),
)
def filter_dr_events_table(
    start_str: str,
    end_str: str,
    min_duration: float,
    max_power: float,
) -> list[EventTableDataEntry]:
    """Filters the DR events table based on user-selected criteria."""
    db_session = readonly_session_factory()
    with db_session() as db:
        query = Select[tuple[PowerTarget]](PowerTarget).order_by(PowerTarget.id.desc())
        if start_str:
            query = query.where(PowerTarget.sql_end_time() >= pd.to_datetime(start_str))
        if end_str:
            query = query.where(PowerTarget.sql_start_time() <= pd.to_datetime(end_str))
        if min_duration:
            query = query.where(
                PowerTarget.sql_duration() >= pd.Timedelta(minutes=min_duration)
            )
        if max_power:
            query = query.where(PowerTarget.subsystem_target <= max_power)
        df = pd.read_sql(query, db.connection())
        if not df.empty:
            df["start_time"] = df["target_period"].apply(lambda x: x.lower)
            df["end_time"] = df["target_period"].apply(lambda x: x.upper)
            df["duration_mins"] = df.apply(
                lambda x: (x["end_time"] - x["start_time"]).total_seconds() / 60,
                axis=1,
            )
            df = df.rename(columns={"subsystem_target": "power_target"})

    if df.empty:
        return []

    return format_table_data(df)


@callback(
    Output("analysis-results-area", "children"),
    [
        Input("analysis-window", "data"),
    ],
    [
        State("analysis-window", "data"),
    ],
    prevent_initial_call=True,
)
def plot_selected_events(
    n_clicks: int, analysis_window: AnalysisWindowData | None
) -> html.Div:
    """Plot the selected DR events for comparison."""
    if not analysis_window:
        raise PreventUpdate

    start_time = datetime.fromisoformat(analysis_window["start"])
    end_time = datetime.fromisoformat(analysis_window["end"])

    # Get all affected jobs
    job_ids = job_ids_in_time_window(start=start_time, end=end_time)

    power_targets = power_targets_in_time_window(
        start=start_time, end=end_time, include_conflicting=True
    )
    power_target_ids = sorted(pt.id for pt in power_targets)

    # Also assign colors to events for visualization
    event_color_map = {
        event_id: COLOR_PALETTE[(i + len(job_ids)) % len(COLOR_PALETTE)]
        for i, event_id in enumerate(power_target_ids)
    }

    # Create event summary cards
    event_summary_cards = []

    for details in power_targets:
        event_id = details.id
        power_target = details.subsystem_target

        # Check if this event is currently active
        now = datetime.now(UTC)
        target_period = details.target_period
        if not target_period.lower or not target_period.upper:
            is_active = False
            duration = None
        else:
            is_active = target_period.lower <= now <= target_period.upper
            duration = target_period.upper - target_period.lower

        card = dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H5(
                                        [
                                            f"Power Target #{event_id}",
                                            html.Span(
                                                " (ACTIVE)",
                                                className="ms-2 text-danger",
                                                style={"fontSize": "0.8rem"},
                                            )
                                            if is_active and not details.superseded_by  # pyright: ignore[reportAttributeAccessIssue]
                                            else None,
                                            html.Span(
                                                f" (Superseded by conflicting ID {details.superseded_by})",  # pyright: ignore[reportAttributeAccessIssue]
                                                className="ms-2 text-danger",
                                                style={"fontSize": "0.8rem"},
                                            )
                                            if details.superseded_by  # pyright: ignore[reportAttributeAccessIssue]
                                            else None,
                                        ],
                                        className="mb-3",
                                    ),
                                    html.P(
                                        [
                                            html.Strong("Target: "),
                                            f"{power_target:.1f} W",
                                        ],
                                        className="mb-2",
                                    ),
                                ],
                                width=6,
                            ),
                            dbc.Col(
                                [
                                    html.P(
                                        [
                                            html.Strong("End: "),
                                            target_period.upper.strftime(
                                                "%Y-%m-%d %H:%M"
                                            )
                                            if target_period.upper
                                            else "Missing",
                                        ],
                                        className="mb-2",
                                    ),
                                    html.P(
                                        [
                                            html.Strong("Start: "),
                                            target_period.lower.strftime(
                                                "%Y-%m-%d %H:%M"
                                            )
                                            if target_period.lower
                                            else "Missing",
                                        ],
                                        className="mb-2",
                                    ),
                                    html.P(
                                        [
                                            html.Strong("Duration: "),
                                            f"{duration.total_seconds() / 60:.0f} mins"
                                            if duration
                                            else "Missing",
                                        ],
                                        className="mb-2",
                                    ),
                                ],
                                width=6,
                            ),
                        ]
                    ),
                ]
            ),
            className="mb-3 mt-2",
            style={"borderLeft": f"5px solid {event_color_map.get(event_id, '#000')}"},
        )
        event_summary_cards.append(card)

    # Combine the event summaries with the plot tabs
    analysis_results = html.Div(
        [
            html.H4("Event Comparison", className="mb-3"),
            html.Div(event_summary_cards),
            dbc.Tabs(
                [
                    dbc.Tab(
                        [
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.Div(
                                            [
                                                html.H6(
                                                    "Power Consumption Summary",
                                                    className="mb-0",
                                                ),
                                                dcc.Dropdown(
                                                    id="power-model-select",
                                                    options=[],
                                                    value=None,  # default: no choice
                                                    placeholder="Select power model",
                                                    clearable=True,
                                                    style={
                                                        "width": "240px",
                                                        "display": "block"
                                                        if is_admin()
                                                        else "none",
                                                    },
                                                    persistence=True,
                                                    persistence_type="session",
                                                ),
                                            ],
                                            className="d-flex justify-content-between align-items-center gap-3",
                                        ),
                                        className="py-2",
                                    ),
                                    dbc.CardBody(
                                        html.Div(
                                            [
                                                html.Div(
                                                    id="sla-violation", className="mb-2"
                                                ),
                                                dcc.Graph(id="summary-power-graph"),
                                                html.Div(
                                                    [
                                                        html.H6(
                                                            "Job-Level Power Display",
                                                            className="mt-4 mb-2",
                                                        ),
                                                        dbc.RadioItems(
                                                            id="job-power-units-toggle",
                                                            options=[
                                                                {
                                                                    "label": "Absolute (W)",
                                                                    "value": "absolute",
                                                                },
                                                                {
                                                                    "label": "Normalized",
                                                                    "value": "normalized",
                                                                },
                                                            ],
                                                            value="absolute",
                                                            persistence_type="memory",
                                                            inline=True,
                                                            className="mb-2",
                                                        ),
                                                        dcc.Graph(id="job-power-graph"),
                                                        dcc.Graph(
                                                            id="job-power-limits-graph"
                                                        ),
                                                        # Add a store for the job power data
                                                        dcc.Store(
                                                            id="job-power-data-store"
                                                        ),
                                                    ],
                                                    id="job-power-container",
                                                    style={
                                                        "display": "block"
                                                        if is_admin()
                                                        else "none"
                                                    },
                                                ),
                                                html.Div(
                                                    [
                                                        html.H6(
                                                            "Throughput Analysis",
                                                            className="mt-4 mb-2",
                                                        ),
                                                        html.P(
                                                            "Tracking Throughput Across Inference & Training Jobs.",
                                                            className="text-muted",
                                                        ),
                                                        dbc.RadioItems(
                                                            id="job-tput-units-toggle",
                                                            options=[
                                                                {
                                                                    "label": "Absolute (W)",
                                                                    "value": "absolute",
                                                                },
                                                                {
                                                                    "label": "Normalized",
                                                                    "value": "normalized",
                                                                },
                                                            ],
                                                            value="absolute",
                                                            persistence_type="memory",
                                                            inline=True,
                                                            className="mb-2",
                                                        ),
                                                        dcc.Graph(
                                                            id="train-tput-graph"
                                                        ),
                                                        dcc.Graph(
                                                            id="inference-gen-tput-graph"
                                                        ),
                                                        dcc.Graph(
                                                            id="inference-prompt-tput-graph"
                                                        ),
                                                    ],
                                                    style={
                                                        "display": "block"
                                                        if is_admin()
                                                        else "none"
                                                    },
                                                ),
                                                html.Div(
                                                    [
                                                        html.H6(
                                                            "Job Priority Grouping Throughput Analysis",
                                                            className="mt-4 mb-2",
                                                        ),
                                                        html.P(
                                                            "Jobs are grouped by priority levels to analyze differences in average normalized throughput.",
                                                            className="text-muted",
                                                        ),
                                                        dbc.RadioItems(
                                                            id="tput-avg-toggle",
                                                            options=[
                                                                {
                                                                    "label": "GPU-Weighted Avg.",
                                                                    "value": "gpu_weighted",
                                                                },
                                                                {
                                                                    "label": "Unweighted Avg.",
                                                                    "value": "unweighted",
                                                                },
                                                            ],
                                                            value="gpu_weighted",
                                                            inline=True,
                                                            className="mb-2",
                                                        ),
                                                        dcc.Graph(
                                                            id="priority-tput-graph"
                                                        ),
                                                    ],
                                                    style={
                                                        "display": "block"
                                                        if is_admin()
                                                        else "none"
                                                    },
                                                ),
                                            ]
                                        )
                                    ),
                                ],
                                className="border-0",
                            )
                        ],
                        label="Power Summary",
                        tab_id="tab-power-summary",
                    ),
                ],
                id="analysis-tabs",
                active_tab="tab-power-summary",
            ),
        ]
    )

    return analysis_results


# Clientside callback to copy shareable link
dash.clientside_callback(
    """
    function(n_clicks, start_value, end_value) {
        if (!n_clicks) {
            return [false, ''];
        }

        // Build the shareable URL with query parameters
        const baseUrl = window.location.origin + window.location.pathname;
        const url = `${baseUrl}?start=${encodeURIComponent(start_value)}&end=${encodeURIComponent(end_value)}`;

        // Copy to clipboard
        navigator.clipboard.writeText(url).then(
            function() {
                console.log('Link copied to clipboard:', url);
            },
            function(err) {
                console.error('Failed to copy link:', err);
            }
        );

        // Show tooltip for 2 seconds
        setTimeout(function() {
            window.dash_clientside.set_props('copy-link-tooltip', {is_open: false});
        }, 2000);

        return [true, url];
    }
    """,
    Output("copy-link-tooltip", "is_open"),
    Output("copy-link-button", "n_clicks"),  # Reset clicks
    Input("copy-link-button", "n_clicks"),
    State("analysis-start-input", "value"),
    State("analysis-end-input", "value"),
    prevent_initial_call=True,
)


# Clientside callback to fix Analyze Now border-radius when Copy Link is hidden
dash.clientside_callback(
    """
    function(copy_button_style) {
        // When copy button is hidden, add rounded class to fix border-radius
        if (copy_button_style && copy_button_style.display === 'none') {
            return 'btn btn-primary btn-sm flex-grow-1 rounded';
        }
        // When copy button is visible, use default btn-group styling
        return 'flex-grow-1';
    }
    """,
    Output("analyze-now-button", "className"),
    Input("copy-link-button", "style"),
    prevent_initial_call=False,
)
