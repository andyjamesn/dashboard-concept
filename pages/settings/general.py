from dash import html, register_page
import emerald_ui_components as eui

register_page(__name__, path='/settings/general', name='General')

layout = html.Div([
    eui.PageHeader(
        heading='General Settings',
        description='Manage your general account settings and preferences.',
        className='p-6 border-b border-border bg-card',
        children=[
            eui.Button(
                variant='outline',
                children=[
                    eui.Icon(name='lucide:rotate-ccw', className='mr-2'),
                    'Reset'
                ]
            ),
            eui.Button(
                children=[
                    eui.Icon(name='lucide:save', className='mr-2'),
                    'Save changes'
                ]
            ),
        ]
    ),
    html.Div([
        eui.Tabs(
            defaultValue='account',
            className='w-full',
            children=[
                eui.TabsList(children=[
                    eui.TabsTrigger(value='account', children='Account'),
                    eui.TabsTrigger(value='password', children='Password'),
            ]),
            eui.TabsContent(
                value='account',
                className='pt-4',
                children=[
                    html.Div([
                        html.Div([
                            eui.Label(htmlFor='marketing', children='Notifications', className='text-base'),
                            html.P('Show Notifications based on your activity',
                                className='text-sm text-muted-foreground'),
                        ], className='space-y-0.5'),
                        eui.Switch(id='marketing'),
        ], className='flex flex-row items-center justify-between rounded-lg border p-4'),
                ]
            ),
            eui.TabsContent(
                value='password',
                className='pt-4',
                children='Change your password here.'
            ),
        ]
    ),
    ], className='p-6'),
], className='flex flex-1 flex-col gap-4')
