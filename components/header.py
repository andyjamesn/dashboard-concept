# Header component and related helpers
from dash import html
import emerald_ui_components as eui


def create_user_nav():
    """Create the user navigation dropdown for the header bar."""
    return eui.DropdownMenu(children=[
        eui.DropdownMenuTrigger(children=[
            eui.Button(
                variant='ghost',
                className='relative h-8 w-8 rounded-full',
                children=[
                    eui.Avatar(
                        className='h-8 w-8',
                        children=[
                            eui.AvatarFallback(children='AN'),
                        ]
                    ),
                ]
            ),
        ]),
        eui.DropdownMenuContent(
            className='w-56 rounded-lg',
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
                                        children='AN'
                                    ),
                                ]
                            ),
                            html.Div([
                                html.Span('Andy Neale', className='truncate font-medium'),
                                html.Span('andy.neale@emeraldai.co', className='truncate text-xs text-muted-foreground'),
                            ], className='grid flex-1 text-left text-sm leading-tight'),
                        ], className='flex items-center gap-2 px-1 py-1.5 text-left text-sm'),
                    ]
                ),
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
    ])


def create_header():
    """Create the main header bar component."""
    return html.Header([
        html.Div([
            eui.SidebarTrigger(id='sidebar-trigger', className='-ml-1'),
            html.Div(className='mx-2 h-4 w-px bg-border'),  # Separator
            # Dynamic breadcrumbs (updated via callback)
            eui.Breadcrumb(id='breadcrumbs'),
        ], className='flex items-center gap-2'),
        # Right side of header - theme toggle and user menu
        html.Div([
            eui.ThemeModeSwitcher(
                id='theme-toggle',
                className='inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors hover:bg-accent hover:text-accent-foreground h-9 w-9'
            ),
            create_user_nav(),
        ], className='ml-auto flex items-center gap-2'),
    ], className='flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-[[data-collapsible=icon]]/sidebar-wrapper:h-12 border-b px-4 bg-card')
