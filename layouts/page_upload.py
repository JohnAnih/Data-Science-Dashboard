import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    'Page Upload',
    dcc.Upload(
        id='upload-file',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ])),
    dbc.Modal([
        dbc.ModalHeader('Upload option'),
        dbc.ModalBody(
            dbc.Input(id='sheet-index', placeholder='Sheet Index', type='number')),
        dbc.ModalFooter([
            dbc.Button('Cancel', id='upload-option-cancel'),
            dbc.Button('Ok', id='upload-option-ok')
        ])], 
        id='modal-upload-option'),
    html.Div(id='alert-upload'),
    html.P(id='debug', children='tes')
])