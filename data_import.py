import os
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_trich_components as dtc

import pandas as pd
import base64
import datetime
import io

dtc.__version__


app = dash.Dash(__name__,
                external_stylesheets = [dbc.themes.BOOTSTRAP])


app.title = "Data Upload"

def learn_more_button():
    return html.Div(
                [
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Supported formats"),
                            dbc.ModalBody(dcc.Markdown("""For now, **ADSML** is supporting only CSV 
                                                       and Excel files only, however,in the future, 
                                                       we plan to support popular database systems 
                                                       like MySQL, Postgres and Microsoft server. 
                                                       If you would like to stay updated, 
                                                       please visit our [blog](#)""")),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="close", className="ml-auto")
                            ),
                        ],
                        id="modal",
                    ),
                ]
            )
    

def create_navbar():
    """
    create_navbar creates the website Navbar using bootsraps components

    To learn more visit: https://dash-bootstrap-components.opensource.faculty.ai/docs/

    Returns
    -------
    NavBar
        creates the website navrbar
    """    ""
    
    # make a reuseable navitem for the different examples
    supported_formats = html.Div(
                                  [
                                    dbc.Button("Learn more", 
                                               id="open", 
                                               color="danger", 
                                               className="mr-1"),

                                    dbc.Tooltip(
                                            """ Click here to learn more about the formats 
                                                accepted on the ADSML platform.
                                            """,
                                            target="open",
                                        ),
                                  ]
                                )
    
    title = html.H2("""
                         DATA IMPORT 
                         """, 
                         style={"color": "white",
                                "font-weight": "bold",
                                "margin-left": "52px",
                                "font-family": 'Montserrat'})


    
    return dbc.Navbar(
                dbc.Container(
                    [
                        html.A(
                            
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src="../assets/Logo.png", 
                                                     height="35px", 
                                                     alt="Automated Data Science and Machine learning blog")),

                                ],
                                align="center",
                                no_gutters=True,
                            ),
                            href="./get-started-page",
                        ),
                        dbc.NavbarToggler(id="navbar-toggler2"),

                        dbc.Collapse(
                            dbc.Nav(
                                [supported_formats, title], 
                                className="ml-auto", 
                                navbar=True
                            ),
                            id="navbar-collapse2",
                            navbar=True,
                        ),
                    ]
                ),
                color="rgb(6, 67, 122)",
                dark=True,
                className="mb-5",
        )

file_upload = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Upload file',style={"text-decoration":"underline"})
        ]),
        style={
            'width': '80%',
            'height': '100px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': 'auto'
        },
        # Allow multiple files to be uploaded
        multiple=False
    ),
    html.Div(id='output-data-upload'),
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

def create_next_buttons():
    """
    create_next_buttons creates the buttons for the other features of the application.
    
    This function makes use of the data_import.css styles

    Returns
    -------
    Buttons
        creates the buttons of disabled and active until the file uploaded
    """    ""
    
    return html.Div( className="feature-buttons",
                     children= [
                                html.Div(className="center",
                                         children= [
                                                    dbc.Button("Data Profling",
                                                               className="btn btn-default",
                                                               style={"margin": "5px"},
                                                               color="primary", 
                                                               active=True),

                                                    dbc.Button("Data visualization", 
                                                               className="btn btn-default",
                                                               style={"margin": "5px"},
                                                               color="primary", 
                                                               disabled=True),

                                                    dbc.Button("Detect common data problems", 
                                                               className="btn btn-default",
                                                               style={"margin": "5px"},
                                                               color="primary", 
                                                               disabled=True),

                                                    dbc.Button("Data Modelling", 
                                                               className="btn btn-default",
                                                               style={"margin": "5px"},
                                                               color="primary", 
                                                               disabled=True)

                                         ]
                                    ,)
                             ], 
    
)

app.layout = html.Div(
    id="data-import",
    
    children= [learn_more_button(),
               create_navbar(), 
               file_upload, 
               create_next_buttons()],

)

@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
    
    
if __name__ == '__main__':
    app.run_server(debug=True,
                   use_reloader=False, 
                   port=8080)