import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    'Landing Page',
    html.Div([
        dcc.Link('Getting Started', href='/upload')
    ])
])