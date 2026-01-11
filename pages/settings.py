from dash import html, register_page

register_page(__name__, path='/settings', name='Settings')

layout = html.Div([
    html.H1('Settings', className='text-3xl font-bold'),
], className='flex flex-1 flex-col gap-4')
