# Catch-all page for nested routes (2 segments) without dedicated page files
# Displays dynamic page header based on navigation config
from dash import html, register_page
import emerald_ui_components as eui

from navigation import get_page_info

# Register as catch-all for 2-segment paths
register_page(
    __name__,
    path_template='/<section>/<page>',
    name='Page',
    order=999
)


def layout(section=None, page=None, **kwargs):
    """Dynamic layout that renders based on the URL path."""
    # Build the full href from path segments
    href = f'/{section}/{page}' if section and page else '/'

    # Look up page info from navigation config
    page_info = get_page_info(href)

    if page_info:
        # Found in navigation - show page header with info
        title = page_info['title']
        description = page_info['description']
        nav_section = page_info['section']
        icon = page_info['icon']
    else:
        # Not found in navigation - show generic 404-style content
        title = 'Page Not Found'
        description = 'This page does not exist in the navigation.'
        nav_section = None
        icon = 'FileQuestion'

    return html.Div([
        # Page Header
        eui.PageHeader(
            heading=title,
            description=description,
            className='p-6 border-b border-border bg-card',
        ),

        # Content area with Coming Soon placeholder
        html.Div([
            eui.Card(
                className='w-full max-w-md',
                children=[
                    eui.CardHeader(
                        children=[
                            html.Div([
                                eui.LucideIcon(name=icon, className='size-8 text-muted-foreground'),
                            ], className='flex items-center justify-center size-16 rounded-full bg-muted mb-4 w-full'),
                            eui.CardTitle(children='Coming Soon'),
                            eui.CardDescription(
                                children=f'The {title} page is under development.'
                            ),
                        ],
                        className='text-center items-center'
                    ),
                    eui.CardContent(
                        children=[
                            html.P(
                                'This feature will be available in a future release.',
                                className='text-center text-muted-foreground'
                            ),
                        ]
                    ),
                ]
            ),
        ], className='flex flex-1 flex-col gap-4 p-6 items-center justify-center'),
    ])
