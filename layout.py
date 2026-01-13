# Main application layout
from dash import dcc, page_container, html
import emerald_ui_components as eui

from components.sidebar import create_sidebar
from components.header import create_header
from navigation import DEFAULT_PERSONA


def create_layout():
    """Create the main application layout with sidebar and content area."""
    return eui.ThemeProvider(
        defaultTheme='system',  # Follows OS preference by default
        storageKey='emerald-ui-theme',
        children=[
            # State storage
            dcc.Location(id='url', refresh=False),
            dcc.Store(id='persona-store', data=DEFAULT_PERSONA, storage_type='local'),

            # Main layout
            eui.SidebarProvider(
                defaultOpen=True,
                children=[
                    # Sidebar
                    create_sidebar(),

                    # Main content area
                    eui.SidebarInset(children=[
                        # Header with trigger, breadcrumbs, and theme toggle
                        create_header(),

                        # Main content - renders the active page
                        html.Div([
                            dcc.Loading(
                                id='page-loading',
                                type='default',
                                children=page_container,
                            ),
                        ], className='flex-1'),
                    ]),
                ]
            ),
        ]
    )
