from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import emerald_ui_components as eui

# Set to False for production (uses pre-built CSS only)
DEBUG = True

# In dev mode, add Tailwind CDN for instant class updates without rebuilding
# In production, only the pre-built CSS from emerald_ui_components is used
external_scripts = (
    ["https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"] if DEBUG else []
)

app = Dash(__name__, external_scripts=external_scripts)

# Sample data
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [2, 4, 1, 3, 5]
})

fig = px.line(df, x="x", y="y", title="Sample Chart")

app.layout = html.Div([
    html.H1("Dash App - Custom Components Demo", className='text-3xl font-bold mb-6'),
    html.P("This demo shows shadcn/ui components in Dash with Tailwind CSS styling.",
           className='text-muted-foreground mb-8'),

    html.Hr(className='my-6'),

    # Button section (shadcn/ui variants)
    html.H2("Button Component", className='text-2xl font-semibold mb-4'),
    html.Div([
        eui.Button(id='btn-default', variant='default', children='Default'),
        eui.Button(id='btn-secondary', variant='secondary', children='Secondary'),
        eui.Button(id='btn-destructive', variant='destructive', children='Destructive'),
        eui.Button(id='btn-outline', variant='outline', children='Outline'),
        eui.Button(id='btn-ghost', variant='ghost', children='Ghost'),
        eui.Button(id='btn-link', variant='link', children='Link'),
    ], className='flex gap-3 flex-wrap mb-6'),

    # Button sizes
    html.H3("Button Sizes", className='text-lg font-medium mb-2'),
    html.Div([
        eui.Button(variant='default', size='sm', children='Small'),
        eui.Button(variant='default', size='default', children='Default'),
        eui.Button(variant='default', size='lg', children='Large'),
    ], className='flex gap-3 items-center mb-6'),

    # Click counter demo
    html.H3("Demo Callbacks", className='text-lg font-medium mb-2'),
    html.Div([
        eui.Button(id='click-counter', variant='default', size='lg', children='Click me!'),
        html.Span(id='click-output', className='ml-4 text-lg'),
    ], className='flex items-center mb-6'),

    # Disabled button
    eui.Button(id='btn-disabled', variant='outline', disabled=True, children='Disabled Button'),

    html.Hr(className='my-6'),

    # Badge section (shadcn/ui variants)
    html.H2("Badge Component", className='text-2xl font-semibold mb-4'),
    html.Div([
        eui.Badge(variant='default', children='Default'),
        eui.Badge(variant='secondary', children='Secondary'),
        eui.Badge(variant='destructive', children='Destructive'),
        eui.Badge(variant='outline', children='Outline'),
    ], className='flex gap-3 flex-wrap mb-6'),

    html.Hr(className='my-6'),

    # Card section (shadcn/ui with sub-components)
    html.H2("Card Component", className='text-2xl font-semibold mb-4'),
    html.Div([
        # Basic Card with Header, Content, Footer
        eui.Card(className='w-80', children=[
            eui.CardHeader(children=[
                eui.CardTitle(children='Welcome'),
                eui.CardDescription(children='Get started with your dashboard'),
            ]),
            eui.CardContent(children=[
                html.P("This is a card with header, content, and footer sections."),
            ]),
            eui.CardFooter(children=[
                eui.Button(variant='default', size='sm', children='Learn More'),
            ]),
        ]),

        # Card with Action button in header
        eui.Card(className='w-80', children=[
            eui.CardHeader(children=[
                eui.CardTitle(children='Statistics'),
                eui.CardDescription(children='Your current stats'),
                eui.CardAction(children=[
                    eui.Button(variant='outline', size='sm', children='Refresh'),
                ]),
            ]),
            eui.CardContent(children=[
                html.Div([
                    eui.Badge(variant='default', children='Active'),
                    html.Span(" 42 users online", className='ml-2'),
                ]),
            ]),
        ]),

        # Simple content-only Card
        eui.Card(className='w-80', children=[
            eui.CardContent(children=[
                html.P("A simple card with only content, no header or footer."),
            ]),
        ]),
    ], className='flex gap-4 flex-wrap mb-6'),

    html.Hr(className='my-6'),

    # Input & Label section (shadcn/ui with 2-way binding)
    html.H2("Input & Label Components", className='text-2xl font-semibold mb-4'),

    # 2-way binding demo
    html.Div([
        html.Div([
            eui.Label(htmlFor='name-input', children='Your Name'),
            eui.Input(id='name-input', placeholder='Enter your name...', value=''),
        ], className='flex flex-col gap-2 mb-4'),

        html.Div([
            html.Span("You typed: ", className='font-medium'),
            html.Span(id='name-output', className='text-primary'),
        ], className='mb-4'),

        # Button to set value programmatically (tests 2-way binding)
        html.Div([
            eui.Button(id='set-name-btn', variant='outline', size='sm', children='Set to "John Doe"'),
        ], className='mb-4'),
    ], className='max-w-sm mb-6'),

    # Other input types
    html.H3("Input Types", className='text-lg font-medium mb-2'),
    html.Div([
        html.Div([
            eui.Label(htmlFor='email-input', children='Email'),
            eui.Input(id='email-input', type='email', placeholder='you@example.com'),
        ], className='flex flex-col gap-2'),

        html.Div([
            eui.Label(htmlFor='password-input', children='Password'),
            eui.Input(id='password-input', type='password', placeholder='Enter password...'),
        ], className='flex flex-col gap-2'),

        html.Div([
            eui.Label(htmlFor='disabled-input', children='Disabled'),
            eui.Input(id='disabled-input', disabled=True, value='Cannot edit'),
        ], className='flex flex-col gap-2'),
    ], className='flex gap-6 flex-wrap mb-6'),

    html.Hr(className='my-6'),

    # Test dropdown
    html.H2("Dash DropDown", className='text-2xl font-semibold mb-4'),
    dcc.Dropdown(
        id="color-input",
        options=["Red", "Green", "Blue"],
        value="Red"
    ),

    html.P(id="color-output", className='mt-2'),

    html.Hr(className='my-6'),

    # Chart
    html.H2("Plotly Chart", className='text-2xl font-semibold mb-4'),
    dcc.Graph(figure=fig)
], className='p-8 font-sans')


@callback(
    Output('click-output', 'children'),
    Input('click-counter', 'n_clicks')
)
def update_click_count(n_clicks):
    if n_clicks is None:
        return 'Button not clicked yet'
    return f'Button clicked {n_clicks} times!'


@callback(
    Output('color-output', 'children'),
    Input('color-input', 'value')
)
def update_color_output(color: str):
    return f'Selected color: {color}'


# 2-way binding: Input value -> display
@callback(
    Output('name-output', 'children'),
    Input('name-input', 'value')
)
def update_name_output(value: str):
    return value or '(empty)'


# 2-way binding: Button click -> set Input value
@callback(
    Output('name-input', 'value'),
    Input('set-name-btn', 'n_clicks'),
    prevent_initial_call=True
)
def set_name_value(n_clicks):
    return 'John Doe'


if __name__ == "__main__":
    app.run(debug=True)  # pyright: ignore[reportUnknownMemberType]
