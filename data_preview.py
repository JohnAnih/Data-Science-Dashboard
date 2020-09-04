import dash_core_components as dcc
import dash_html_components as html
from data_import import create_navbar, create_next_buttons

preview_layout = html.Div([
	create_navbar('DATA PREVIEW'),
    dcc.Input(id='trigger-preview', style={'display': 'none'}),
    html.Div(id='output-data-overview'),
	create_next_buttons(True),
])