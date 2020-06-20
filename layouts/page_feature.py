import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    'Page Feature',
    html.Div([
        dbc.Row([
            html.A(html.Div('Data Profiling and Understanding', className='feature-menu'), href='/data_profiling'),
            html.A(html.Div('Fix Data Problems', className='feature-menu'), href='/')
        ]),
        dbc.Row([
            html.A(html.Div('Data Visualization', className='feature-menu'), href='/'),
            html.A(html.Div('Perform Predictions', className='feature-menu'), href='/')
        ])
    ]),
    html.Div(id='data-overview')
])