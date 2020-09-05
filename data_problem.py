import dash_core_components as dcc
import dash_html_components as html
from data_import import create_navbar, create_next_buttons

dataproblem_layout = html.Div([
    html.Div(id='debugs'),
    create_navbar('DATA PROBLEM'),
    dcc.Input(id='trigger-problem', style={'display': 'none'}),
    html.Div(id='output-data-problem', style= {'margin-left': '6%'}),
    create_next_buttons(True)
])