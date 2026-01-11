# Application callbacks
from dash import callback, Input, Output, page_registry
import emerald_ui_components as eui


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
