from dash import html, register_page, dcc

register_page(__name__, path='/', name='Home')

layout = html.Div([
    dcc.Location(id='redirect-home', pathname='/cluster/overview', refresh=True),
])
