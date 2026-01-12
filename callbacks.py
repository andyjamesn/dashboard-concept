# Application callbacks
from dash import callback, Input, Output, State, page_registry, ctx, no_update
import emerald_ui_components as eui

from navigation import PERSONAS, DEFAULT_PERSONA
from components.sidebar import create_nav_menu, create_persona_switcher


# =============================================================================
# BREADCRUMB CALLBACK
# =============================================================================

@callback(
    Output('breadcrumbs', 'children'),
    Input('url', 'pathname')
)
def update_breadcrumbs(pathname):
    """Generate breadcrumb trail from URL path segments."""
    # Handle root path
    if pathname == '/':
        return eui.BreadcrumbList(children=[
            eui.BreadcrumbItem(children=[
                eui.BreadcrumbPage(children='Home'),
            ]),
        ])

    # Build breadcrumb trail from path segments
    segments = [s for s in pathname.split('/') if s]
    items = [
        eui.BreadcrumbItem(className='hidden md:block', children=[
            eui.BreadcrumbLink(href='/', children='Home'),
        ]),
    ]

    path_so_far = ''
    for i, segment in enumerate(segments):
        path_so_far += f'/{segment}'
        items.append(eui.BreadcrumbSeparator(className='hidden md:block'))

        # Look up display name from page registry
        name = segment.replace('-', ' ').title()
        for page in page_registry.values():
            if page['path'] == path_so_far:
                name = page['name']
                break

        # Last segment is current page (not a link)
        if i == len(segments) - 1:
            items.append(eui.BreadcrumbItem(children=[
                eui.BreadcrumbPage(children=name),
            ]))
        else:
            items.append(eui.BreadcrumbItem(className='hidden md:block', children=[
                eui.BreadcrumbLink(href=path_so_far, children=name),
            ]))

    return eui.BreadcrumbList(children=items)


# =============================================================================
# PERSONA SWITCHING CALLBACK
# =============================================================================

@callback(
    Output('persona-store', 'data'),
    [Input(persona['id'], 'n_clicks') for persona in PERSONAS],
    State('persona-store', 'data'),
    prevent_initial_call=True
)
def switch_persona(*args):
    """Handle persona switching when a persona menu item is clicked."""
    # Last arg is the current persona state
    current_persona = args[-1]

    # Check if this was an actual click (not a component re-render)
    if not ctx.triggered:
        return no_update

    triggered = ctx.triggered[0]
    triggered_id = ctx.triggered_id

    # Ignore if no real click happened (value is None or 0 from re-render)
    if not triggered_id or not triggered.get('value'):
        return no_update

    # Find the matching persona
    for persona in PERSONAS:
        if persona['id'] == triggered_id:
            # Only update if actually changing to a different persona
            if current_persona and current_persona.get('id') == persona['id']:
                return no_update
            return persona

    return no_update


@callback(
    Output('sidebar-nav-menu', 'children'),
    Input('persona-store', 'data'),
    Input('url', 'pathname')
)
def update_navigation(persona_data, pathname):
    """Update the sidebar navigation when persona or URL changes."""
    if not persona_data:
        persona_data = DEFAULT_PERSONA

    persona_key = persona_data.get('key', DEFAULT_PERSONA['key'])
    return [create_nav_menu(persona_key, pathname)]


@callback(
    Output('sidebar-persona-switcher', 'children'),
    Input('persona-store', 'data')
)
def update_persona_switcher(persona_data):
    """Update the persona switcher display when persona changes."""
    if not persona_data:
        persona_data = DEFAULT_PERSONA

    return [create_persona_switcher(persona_data)]
