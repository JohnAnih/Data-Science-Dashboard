from layouts.import_libs import *
from data_import import create_navbar, create_next_buttons

data_viz_layout = html.Div(
                             [
                             create_navbar('DATA VISUALIZATION'),
                             
                             html.H3('Data Visualization', 
                                     style={'color': 'rgb(6, 67, 122)', 
                                            'padding-bottom': '2%', 
                                            'margin-bottom': '1%', 
                                            'margin-left': '10%'}),
                             
                             html.Button('Add Chart',
                                         id='add-chart', 
                                         n_clicks=0, 
                                         style={'width': '10%', 
                                                'height': '28px', 
                                                'margin-left': '10%', 
                                                'color': 'white',
                                                'margin-bottom': '4%',
                                                'background-color': 'rgb(6, 67, 122)'}),
                             
                             html.Div(id='output-data-visualization', 
                                      children=[], 
                                      style= {'margin-left': '10%'}),
                             
                             create_next_buttons(True)
                         ]
                     )