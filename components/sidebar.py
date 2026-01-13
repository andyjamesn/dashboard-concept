# Sidebar component and related helpers
from dash import html, dcc
import emerald_ui_components as eui

from navigation import PERSONAS, DEFAULT_PERSONA, get_navigation_for_persona


def create_sub_item(sub_item, current_path=None):
    """Create a sub-menu item, optionally wrapped in dcc.Link for navigation."""
    # Check if this item is active (matches current URL)
    is_active = current_path and sub_item.get('href') == current_path

    button = eui.SidebarMenuSubButton(
        id=sub_item['id'],
        children=sub_item['title'],
        isActive=is_active
    )
    # If item has href, wrap in dcc.Link for client-side navigation
    if 'href' in sub_item:
        return eui.SidebarMenuSubItem(children=[
            dcc.Link(button, href=sub_item['href'], style={'textDecoration': 'none'})
        ])
    return eui.SidebarMenuSubItem(children=[button])


def create_nav_item(item, current_path=None):
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
                        create_sub_item(sub_item, current_path) for sub_item in item.get('items', [])
                    ]),
                ]),
            ]),
        ]
    )


def create_nav_menu(persona_key: str, current_path: str = None):
    """Create the navigation menu for a given persona."""
    nav_items = get_navigation_for_persona(persona_key)
    return eui.SidebarMenu(children=[
        create_nav_item(item, current_path) for item in nav_items
    ])


def create_persona_switcher(current_persona=None):
    """Create the persona switcher dropdown in sidebar footer."""
    if current_persona is None:
        current_persona = DEFAULT_PERSONA

    # Build menu items for each persona
    persona_items = []
    for persona in PERSONAS:
        persona_items.append(
            eui.DropdownMenuItem(
                id=persona['id'],
                className='gap-2 p-2',
                children=[
                    html.Div([
                        html.Div(className=f'size-2 rounded-full {persona["color"]}'),
                    ], className='flex size-6 items-center justify-center rounded-md border'),
                    html.Div([
                        html.Span(persona['name'], className='font-medium'),
                        html.Span(persona['description'], className='text-xs text-muted-foreground'),
                    ], className='grid flex-1 text-left leading-tight'),
                    eui.DropdownMenuShortcut(children=persona['shortcut']),
                ]
            )
        )

    return eui.SidebarMenu(children=[
        eui.SidebarMenuItem(children=[
            eui.DropdownMenu(children=[
                eui.DropdownMenuTrigger(children=[
                    eui.SidebarMenuButton(
                        size='lg',
                        className='data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground',
                        children=[
                            html.Div([
                                html.Div(className=f'size-3 rounded-full {current_persona["color"]}'),
                            ], className='flex aspect-square size-8 items-center justify-center rounded-lg bg-muted text-sidebar-primary-foreground'),
                            html.Div([
                                html.Span(current_persona['name'], className='truncate font-medium'),
                                html.Span(current_persona['description'], className='truncate text-xs text-muted-foreground'),
                            ], className='grid flex-1 text-left text-sm leading-tight'),
                            eui.LucideIcon(name='ChevronsUpDown', className='ml-auto'),
                        ]
                    ),
                ]),
                eui.DropdownMenuContent(
                    className='w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg',
                    side='top',
                    align='start',
                    sideOffset=4,
                    children=[
                        eui.DropdownMenuLabel(
                            className='text-xs text-muted-foreground',
                            children='Switch Persona'
                        ),
                        *persona_items,
                    ]
                ),
            ]),
        ]),
    ])


def create_sidebar():
    """Create the main sidebar component."""
    return eui.Sidebar(
        side='left',
        collapsible='icon',
        children=[
            # Sidebar Header - Logo
            eui.SidebarHeader(children=[
                # Full logo - hidden when collapsed, switches between light/dark versions
                html.Div([
                    # Light mode logo (dark text) - visible in light theme only
                    html.Img(
                        src='/assets/images/emerald-logo-full.svg',
                        className='h-8 logo-light'
                    ),
                    # Dark mode logo (white text) - visible in dark theme only
                    html.Img(
                        src='/assets/images/emerald-logo-full-reversed.svg',
                        className='h-8 logo-dark'
                    ),
                ], className='flex items-center justify-center group-data-[collapsible=icon]:hidden bg-card -m-2 h-16 border-b'),
                # Widget logo - only shown when collapsed (same for both modes)
                html.Div([
                    html.Img(src='/assets/images/emerald-logo-widget.svg', className='size-8'),
                ], className='hidden items-center group-data-[collapsible=icon]:flex'),
            ]),

            # Sidebar Content - Navigation
            eui.SidebarContent(children=[
                # Platform Group with collapsible items - dynamic based on persona
                eui.SidebarGroup(children=[
                    eui.SidebarGroupLabel(children='Platform'),
                    # Navigation menu container - updated by callback
                    html.Div(
                        id='sidebar-nav-menu',
                        children=[create_nav_menu(DEFAULT_PERSONA['key'])]
                    ),
                ]),
            ]),

            # Sidebar Footer - Persona switcher (updated by callback)
            eui.SidebarFooter(
                id='sidebar-persona-switcher',
                children=[create_persona_switcher()]
            ),

            # Rail for collapse interaction
            eui.SidebarRail(),
        ]
    )
