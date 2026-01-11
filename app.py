from dash import Dash, html, dcc, page_container, page_registry, callback, Input, Output
import emerald_ui_components as eui

# Set to False for production (uses pre-built CSS only)
DEBUG = True

# In dev mode, add Tailwind CDN for instant class updates without rebuilding
# In production, only the pre-built CSS from emerald_ui_components is used
external_scripts = (
    ["https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"] if DEBUG else []
)

app = Dash(__name__, external_scripts=external_scripts, use_pages=True, pages_folder='pages')

# Icons use Lucide icon names - see https://lucide.dev/icons
NAV_MAIN = [
    {
        'title': 'Cluster',
        'icon': 'Server',
        'isActive': True,
        'items': [
            {'title': 'Overview', 'id': 'nav-overview', 'href': '/'},
            {'title': 'Starred', 'id': 'nav-starred'},
            {'title': 'Settings', 'id': 'nav-settings'},
        ]
    },
    {
        'title': 'Forecast',
        'icon': 'CloudLightning',
        'isActive': True,
        'items': [
            {'title': 'Genesis', 'id': 'nav-genesis'},
            {'title': 'Explorer', 'id': 'nav-explorer'},
            {'title': 'Quantum', 'id': 'nav-quantum'},
        ]
    },
    {
        'title': 'Documentation',
        'icon': 'BookOpen',
        'items': [
            {'title': 'Introduction', 'id': 'nav-intro'},
            {'title': 'Get Started', 'id': 'nav-getstarted'},
            {'title': 'Tutorials', 'id': 'nav-tutorials'},
            {'title': 'Changelog', 'id': 'nav-changelog'},
        ]
    },
    {
        'title': 'Settings',
        'icon': 'Settings2',
        'items': [
            {'title': 'General', 'id': 'nav-general', 'href': '/settings/general'},
            {'title': 'Team', 'id': 'nav-team'},
            {'title': 'Billing', 'id': 'nav-billing'},
            {'title': 'Limits', 'id': 'nav-limits'},
        ]
    },
]

PROJECTS = [
    {'name': 'Design Engineering', 'icon': 'Frame', 'id': 'proj-design'},
    {'name': 'Sales & Marketing', 'icon': 'PieChart', 'id': 'proj-sales'},
]


def create_sub_item(sub_item):
    """Create a sub-menu item, optionally wrapped in dcc.Link for navigation."""
    button = eui.SidebarMenuSubButton(
        id=sub_item['id'],
        children=sub_item['title']
    )
    # If item has href, wrap in dcc.Link for client-side navigation
    if 'href' in sub_item:
        return eui.SidebarMenuSubItem(children=[
            dcc.Link(button, href=sub_item['href'], style={'textDecoration': 'none'})
        ])
    return eui.SidebarMenuSubItem(children=[button])


def create_nav_item(item):
    """Create a collapsible navigation item with sub-items."""
    return eui.Collapsible(
        defaultOpen=item.get('isActive', False),
        className='group/collapsible',
        children=[
            eui.SidebarMenuItem(children=[
                eui.CollapsibleTrigger(children=[
                    eui.SidebarMenuButton(
                        tooltip=item['title'],
                        children=[
                            eui.LucideIcon(name=item['icon']),
                            html.Span(item['title']),
                            eui.LucideIcon(
                                name='ChevronRight',
                                className='ml-auto transition-transform duration-200 group-data-[state=open]/collapsible:rotate-90'
                            ),
                        ]
                    ),
                ]),
                eui.CollapsibleContent(children=[
                    eui.SidebarMenuSub(children=[
                        create_sub_item(sub_item) for sub_item in item.get('items', [])
                    ]),
                ]),
            ]),
        ]
    )


def create_team_switcher():
    """Create the team switcher dropdown in sidebar header."""
    return eui.SidebarMenu(children=[
        eui.SidebarMenuItem(children=[
            eui.DropdownMenu(children=[
                eui.DropdownMenuTrigger(children=[
                    eui.SidebarMenuButton(
                        size='lg',
                        className='data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground',
                        children=[
                            html.Div([
                                eui.LucideIcon(name='GalleryVerticalEnd', className='size-4'),
                            ], className='flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground'),
                            html.Div([
                                html.Span('Acme Inc', className='truncate font-medium'),
                                html.Span('Enterprise', className='truncate text-xs'),
                            ], className='grid flex-1 text-left text-sm leading-tight'),
                            eui.LucideIcon(name='ChevronsUpDown', className='ml-auto'),
                        ]
                    ),
                ]),
                eui.DropdownMenuContent(
                    className='w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg',
                    side='bottom',
                    align='start',
                    sideOffset=4,
                    children=[
                        eui.DropdownMenuLabel(
                            className='text-xs text-muted-foreground',
                            children='Teams'
                        ),
                        eui.DropdownMenuItem(
                            id='team-acme',
                            className='gap-2 p-2',
                            children=[
                                html.Div([
                                    eui.LucideIcon(name='GalleryVerticalEnd', className='size-4 shrink-0'),
                                ], className='flex size-6 items-center justify-center rounded-md border'),
                                html.Span('Acme Inc'),
                                eui.DropdownMenuShortcut(children='⌘1'),
                            ]
                        ),
                        eui.DropdownMenuItem(
                            id='team-acme-corp',
                            className='gap-2 p-2',
                            children=[
                                html.Div([
                                    eui.LucideIcon(name='AudioWaveform', className='size-4 shrink-0'),
                                ], className='flex size-6 items-center justify-center rounded-md border'),
                                html.Span('Acme Corp.'),
                                eui.DropdownMenuShortcut(children='⌘2'),
                            ]
                        ),
                        eui.DropdownMenuItem(
                            id='team-evil',
                            className='gap-2 p-2',
                            children=[
                                html.Div([
                                    eui.LucideIcon(name='Command', className='size-4 shrink-0'),
                                ], className='flex size-6 items-center justify-center rounded-md border'),
                                html.Span('Evil Corp.'),
                                eui.DropdownMenuShortcut(children='⌘3'),
                            ]
                        ),
                        eui.DropdownMenuSeparator(),
                        eui.DropdownMenuItem(
                            id='add-team',
                            className='gap-2 p-2',
                            children=[
                                html.Div([
                                    eui.LucideIcon(name='Plus', className='size-4'),
                                ], className='flex size-6 items-center justify-center rounded-md border bg-transparent'),
                                html.Span('Add team', className='text-muted-foreground font-medium'),
                            ]
                        ),
                    ]
                ),
            ]),
        ]),
    ])


def create_user_nav():
    """Create the user navigation dropdown in sidebar footer."""
    return eui.SidebarMenu(children=[
        eui.SidebarMenuItem(children=[
            eui.DropdownMenu(children=[
                eui.DropdownMenuTrigger(children=[
                    eui.SidebarMenuButton(
                        size='lg',
                        className='data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground',
                        children=[
                            eui.Avatar(
                                className='h-8 w-8 rounded-lg',
                                children=[
                                    eui.AvatarFallback(
                                        className='rounded-lg',
                                        children='CN'
                                    ),
                                ]
                            ),
                            html.Div([
                                html.Span('Andy Neale', className='truncate font-medium'),
                                html.Span('andy.neale@emeraldai.co', className='truncate text-xs'),
                            ], className='grid flex-1 text-left text-sm leading-tight'),
                            eui.LucideIcon(name='ChevronsUpDown', className='ml-auto size-4'),
                        ]
                    ),
                ]),
                eui.DropdownMenuContent(
                    className='w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg',
                    side='bottom',
                    align='end',
                    sideOffset=4,
                    children=[
                        eui.DropdownMenuLabel(
                            className='p-0 font-normal',
                            children=[
                                html.Div([
                                    eui.Avatar(
                                        className='h-8 w-8 rounded-lg',
                                        children=[
                                            eui.AvatarFallback(
                                                className='rounded-lg',
                                                children='CN'
                                            ),
                                        ]
                                    ),
                                    html.Div([
                                        html.Span('Andy Neale', className='truncate font-medium'),
                                        html.Span('andy.neale@emeraldai.co', className='truncate text-xs'),
                                    ], className='grid flex-1 text-left text-sm leading-tight'),
                                ], className='flex items-center gap-2 px-1 py-1.5 text-left text-sm'),
                            ]
                        ),
                        eui.DropdownMenuSeparator(),
                        eui.DropdownMenuGroup(children=[
                            eui.DropdownMenuItem(
                                id='user-upgrade',
                                children=[
                                    eui.LucideIcon(name='Sparkles'),
                                    html.Span('Upgrade to Pro'),
                                ]
                            ),
                        ]),
                        eui.DropdownMenuSeparator(),
                        eui.DropdownMenuGroup(children=[
                            eui.DropdownMenuItem(
                                id='user-account',
                                children=[
                                    eui.LucideIcon(name='BadgeCheck'),
                                    html.Span('Account'),
                                ]
                            ),
                            eui.DropdownMenuItem(
                                id='user-billing',
                                children=[
                                    eui.LucideIcon(name='CreditCard'),
                                    html.Span('Billing'),
                                ]
                            ),
                            eui.DropdownMenuItem(
                                id='user-notifications',
                                children=[
                                    eui.LucideIcon(name='Bell'),
                                    html.Span('Notifications'),
                                ]
                            ),
                        ]),
                        eui.DropdownMenuSeparator(),
                        eui.DropdownMenuItem(
                            id='user-logout',
                            children=[
                                eui.LucideIcon(name='LogOut'),
                                html.Span('Log out'),
                            ]
                        ),
                    ]
                ),
            ]),
        ]),
    ])


# Main application layout with sidebar-07 style
# Wrapped in ThemeProvider for light/dark mode support
app.layout = eui.ThemeProvider(
    defaultTheme='system',  # Follows OS preference by default
    storageKey='emerald-ui-theme',
    children=[
        dcc.Location(id='url', refresh=False),
        eui.SidebarProvider(
            defaultOpen=True,
            children=[
                # Sidebar
                eui.Sidebar(
                    side='left',
                    collapsible='icon',
                    children=[
                        # Sidebar Header - Team Switcher
                        eui.SidebarHeader(children=[
                            # Full logo - hidden when collapsed, switches between light/dark versions
                            html.Div([
                                # Light mode logo (dark text)
                                html.Img(src='/assets/images/emerald-logo-full.svg', className='h-8 dark:hidden'),
                                # Dark mode logo (white text)
                                html.Img(src='/assets/images/emerald-logo-full-reversed.svg', className='h-8 hidden dark:block'),
                            ], className='flex items-center justify-center group-data-[collapsible=icon]:hidden bg-card -m-2 h-16 border-b'),
                            # Widget logo - only shown when collapsed (same for both modes)
                            html.Div([
                                html.Img(src='/assets/images/emerald-logo-widget.svg', className='size-8'),
                            ], className='hidden items-center group-data-[collapsible=icon]:flex'),

                            # create_team_switcher(),
                        ]),

                        # Sidebar Content - Navigation
                        eui.SidebarContent(children=[
                            # Platform Group with collapsible items
                            eui.SidebarGroup(children=[
                                eui.SidebarGroupLabel(children='Platform'),
                                eui.SidebarMenu(children=[
                                    create_nav_item(item) for item in NAV_MAIN
                                ]),
                            ]),

                            # Projects Group (hidden when collapsed)
                            eui.SidebarGroup(
                                className='group-data-[collapsible=icon]:hidden',
                                children=[
                                    eui.SidebarGroupLabel(children='Projects'),
                                    eui.SidebarMenu(children=[
                                        eui.SidebarMenuItem(children=[
                                            eui.SidebarMenuButton(
                                                id=project['id'],
                                                children=[
                                                    eui.LucideIcon(name=project['icon']),
                                                    html.Span(project['name']),
                                                ]
                                            ),
                                        ]) for project in PROJECTS
                                    ]),
                                ]
                            ),
                        ]),

                        # Sidebar Footer - User profile
                        eui.SidebarFooter(children=[
                            create_user_nav(),
                        ]),

                        # Rail for collapse interaction
                        eui.SidebarRail(),
                    ]
                ),

                # Main content area
                eui.SidebarInset(children=[
                    # Header with trigger, breadcrumbs, and theme toggle
                    html.Header([
                        html.Div([
                            eui.SidebarTrigger(id='sidebar-trigger', className='-ml-1'),
                            html.Div(className='mx-2 h-4 w-px bg-border'),  # Separator
                            # Dynamic breadcrumbs (updated via callback)
                            eui.Breadcrumb(id='breadcrumbs'),
                        ], className='flex items-center gap-2'),
                        # Theme toggle on the right side of header
                        html.Div([
                            eui.ThemeModeSwitcher(
                                id='theme-toggle',
                                className='inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors hover:bg-accent hover:text-accent-foreground h-9 w-9'
                            ),
                        ], className='ml-auto'),
                    ], className='flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-[[data-collapsible=icon]]/sidebar-wrapper:h-12 border-b px-4 bg-card'),

                    # Main content - renders the active page
                    html.Div([
                        page_container,
                    ], className='flex-1 p-4'),
                ]),
            ]
        ),
    ]
)


# Callback to update breadcrumbs based on current URL
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


if __name__ == "__main__":
    app.run(debug=True, port=8052)  # pyright: ignore[reportUnknownMemberType]
