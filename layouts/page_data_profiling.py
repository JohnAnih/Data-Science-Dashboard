import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    'Page Data Profiling',
    dcc.Input(id='trigger-dashboard', style={'display': 'none'}),
    html.Br(),
    html.Div(id='data-overview'),
])