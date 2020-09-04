import dash_core_components as dcc
import dash_html_components as html
from data_import import create_navbar, create_next_buttons

profiling_layout = html.Div([
    create_navbar('DATA PROFILING'),
    dcc.Input(id='trigger-profiling', style={'display': 'none'}),
    html.Div(id='output-data-profiling'),
    create_next_buttons(True)
])