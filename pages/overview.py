from dash import html, register_page, callback, Input, Output
import emerald_ui_components as eui

register_page(__name__, path='/', name='Overview')

layout = html.Div([
    # html.H3(children='Welcome to Emerald AI', className='text-4xl'),
    html.Div([
        eui.Card(
            children=[
                eui.CardContent(
                    children=[
                        html.Div(
                            children=[
                                html.Div(children=eui.LucideIcon(name='ClockFading', size=36, className='text-rose-200'), className='size-16 flex items-center shrink-0 justify-center bg-rose-900 rounded-full p-1 aspect-[1/1]'),
                                html.P(children='Pending', className='uppercase'),
                                html.P(children='3', className='text-6xl font-normal'),
                            ],
                            className='w-full flex gap-2 justify-between'
                        )
                    ]
                )
            ]
        ),
        eui.Card(
            children=[
                eui.CardContent(
                    children=[
                        html.Div(
                            children=[
                                html.Div(children=eui.LucideIcon(name='CircleFadingArrowUp', size=36, className='text-indigo-200'), className='size-16 flex items-center shrink-0 justify-center bg-indigo-900 rounded-full p-1 aspect-[1/1]'),
                                html.P(children='7', className='text-6xl font-normal'),
                            ],
                            className='w-full flex gap-2 justify-between'
                        )
                    ]
                )
            ]
        ),
        eui.Card(
            children=[
                eui.CardContent(
                    children=[
                        html.Div(
                            children=[
                                html.Div(children=eui.LucideIcon(name='CheckCheck', size=36, className='text-lime-200'), className='size-16 flex items-center shrink-0 justify-center bg-lime-800 rounded-full p-1 aspect-[1/1]'),
                                html.P(children='5', className='text-6xl font-normal'),
                            ],
                            className='w-full flex gap-2 justify-between'
                        )
                    ]
                )
            ]
        ),
        eui.Card(
            children=[
                eui.CardContent(
                    children=[
                        html.Div(
                            children=[
                                html.Div(children=eui.LucideIcon(name='FileQuestionMark', size=36, className='text-teal-200'), className='size-16 flex items-center shrink-0 justify-center bg-teal-900 rounded-full p-1 aspect-[1/1]'),
                                html.P(children='0', className='text-6xl font-normal'),
                            ],
                            className='w-full flex gap-2 justify-between'
                        )
                    ]
                )
            ]
        )
    ], className='grid auto-rows-min gap-4 md:grid-cols-4'),
    html.Div(className='min-h-[100vh] flex-1 rounded-xl bg-muted opacity-50 md:min-h-min'),

    eui.Card(children=[
        eui.CardHeader(children=[
            eui.CardTitle(children='Navigation Status'),
            eui.CardDescription(children='Click a menu item to see it here'),
        ]),
        eui.CardContent(children=[
            html.P(id='nav-status', className='text-muted-foreground',
                   children='Click a menu item to see it here'),
        ]),
    ]),
], className='flex flex-1 flex-col gap-4 p-4')


# Callback to show which menu item was clicked
@callback(
    Output('nav-status', 'children'),
    [
        # Sub-menu items
        Input('nav-history', 'n_clicks'),
        Input('nav-starred', 'n_clicks'),
        Input('nav-settings', 'n_clicks'),
        Input('nav-genesis', 'n_clicks'),
        Input('nav-explorer', 'n_clicks'),
        Input('nav-quantum', 'n_clicks'),
        Input('nav-intro', 'n_clicks'),
        Input('nav-getstarted', 'n_clicks'),
        Input('nav-tutorials', 'n_clicks'),
        Input('nav-changelog', 'n_clicks'),
        Input('nav-general', 'n_clicks'),
        Input('nav-team', 'n_clicks'),
        Input('nav-billing', 'n_clicks'),
        Input('nav-limits', 'n_clicks'),
        # Projects
        Input('proj-design', 'n_clicks'),
        Input('proj-sales', 'n_clicks'),
        # User dropdown
        Input('user-upgrade', 'n_clicks'),
        Input('user-account', 'n_clicks'),
        Input('user-billing', 'n_clicks'),
        Input('user-notifications', 'n_clicks'),
        Input('user-logout', 'n_clicks'),
    ],
    prevent_initial_call=True
)
def update_nav_status(*args):
    from dash import ctx
    triggered_id = ctx.triggered_id

    labels = {
        # Playground
        'nav-history': 'Playground > History',
        'nav-starred': 'Playground > Starred',
        'nav-settings': 'Playground > Settings',
        # Models
        'nav-genesis': 'Models > Genesis',
        'nav-explorer': 'Models > Explorer',
        'nav-quantum': 'Models > Quantum',
        # Documentation
        'nav-intro': 'Documentation > Introduction',
        'nav-getstarted': 'Documentation > Get Started',
        'nav-tutorials': 'Documentation > Tutorials',
        'nav-changelog': 'Documentation > Changelog',
        # Settings
        'nav-general': 'Settings > General',
        'nav-team': 'Settings > Team',
        'nav-billing': 'Settings > Billing',
        'nav-limits': 'Settings > Limits',
        # Projects
        'proj-design': 'Project: Design Engineering',
        'proj-sales': 'Project: Sales & Marketing',
        # User
        'user-upgrade': 'Action: Upgrade to Pro',
        'user-account': 'Navigate: Account',
        'user-billing': 'Navigate: Billing',
        'user-notifications': 'Navigate: Notifications',
        'user-logout': 'Action: Log out',
    }

    return f'You clicked: {labels.get(triggered_id, "Unknown")}'
