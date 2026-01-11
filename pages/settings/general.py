from dash import html, register_page
import emerald_ui_components as eui

register_page(__name__, path='/settings/general', name='General')

layout = html.Div([
    eui.PageHeader(
        heading='General Settings',
        description='Manage your general account settings and preferences.',
    ),
], className='flex flex-1 flex-col gap-4')
