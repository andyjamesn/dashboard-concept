# Dynamically register stub pages for navigation items without dedicated pages
from dash import html, register_page
import emerald_ui_components as eui

from navigation import PERSONA_NAVIGATION

# Pages that have real implementations (don't create stubs for these)
EXISTING_PAGES = {
    '/',
    '/cluster/overview',
    '/settings/general',
}

# Collect all hrefs from navigation config
NAV_HREFS = set()
for nav_items in PERSONA_NAVIGATION.values():
    for section in nav_items:
        for item in section.get('items', []):
            if 'href' in item:
                NAV_HREFS.add(item['href'])

# Stub pages to create (nav hrefs minus existing pages)
STUB_HREFS = NAV_HREFS - EXISTING_PAGES


def create_stub_layout(href: str, title: str, description: str, icon: str):
    """Create a stub layout function for a given page."""
    def layout():
        return html.Div([
            eui.PageHeader(
                heading=title,
                description=description,
                className='p-6 border-b border-border bg-card',
            ),
            html.Div([
                eui.Card(
                    className='w-full max-w-md',
                    children=[
                        eui.CardHeader(
                            children=[
                                html.Div([
                                    html.Div([
                                        eui.LucideIcon(name=icon, className='size-8 text-muted-foreground'),
                                    ], className='flex items-center justify-center size-16 rounded-full bg-muted mb-4'),
                                ], className='flex items-center justify-center'),
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
    return layout


# Register stub pages for each missing nav item
for nav_items in PERSONA_NAVIGATION.values():
    for section in nav_items:
        for item in section.get('items', []):
            href = item.get('href')
            if href and href in STUB_HREFS:
                # Create unique module name from href
                module_name = f"pages.stub_{href.replace('/', '_').strip('_')}"
                register_page(
                    module_name,
                    path=href,
                    name=item['title'],
                    layout=create_stub_layout(
                        href=href,
                        title=item['title'],
                        description=item.get('description', ''),
                        icon=section.get('icon', 'File')
                    )
                )
                # Remove from STUB_HREFS so we don't register duplicates
                STUB_HREFS.discard(href)
