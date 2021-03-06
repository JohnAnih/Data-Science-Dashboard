from layouts.import_libs import *

from layouts import markdowns

def learn_more_button():
    """
    learn_more_button creates the learn more button that informs users

    about the accepted formats on the ADSML platform.

    Returns
    -------
    Button
        Bootstrap modal button
    """    ""
    return html.Div(
                [
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Supported formats"),
                            dbc.ModalBody(dcc.Markdown(markdowns.data_import_learn_more)),
                            dbc.ModalFooter(
                                dbc.Button("Close", 
                                           id="learn-more-close-button-data-import", 
                                           className="ml-auto")
                            ),
                        ],
                        id="data-import-learn-more-button",
                        scrollable=True,
                    ),
                ]
            )
    

def create_navbar(title):
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
                                               id="learn-more-button", 
                                               color="danger", 
                                               className="mr-1"),

                                    dbc.Tooltip(
                                            """ Click here to learn more about the input data sources 
                                                currently accepted on the ADSML platform.
                                            """,
                                            target="learn-more-button",
                                        ),
                                  ],
                                  style = {'display': 'inherit' if title == 'DATA IMPORT' else 'none'}
                                )
    
    title = html.H2(title, 
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
                            href="/",
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

def file_upload():
    """
    file_upload allows the user to upload files into the web application

    """    ""

    return html.Div([
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div([
                            'Drag and Drop or ',
                            html.A('Upload file',
                                   style={"text-decoration":"underline"})
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
                        # Allow one file at a time
                        multiple=False
                    ),
                    
                    dbc.Modal(
                        [
                        dbc.ModalHeader('Upload option'),
                        
                        dbc.ModalBody(
                            dbc.Input(id='sheet-index', 
                                      placeholder='Sheet Index', 
                                      type='number')),
                        
                        dbc.ModalFooter([
                            dbc.Button('Cancel', id='upload-option-cancel'),
                            dbc.Button('Ok', id='upload-option-ok')
                                ]
                            )
                        ], 
                        id='modal-upload-option'
                              
                    ),
                    
                    html.Div(id='alert-upload'),
                    html.Div(id='output-data-upload'),
                ]
                    )


def create_next_buttons(uploaded=False):
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
                                 
                                                    
                                                    dcc.Link(
														dbc.Button("Home Page",
                                                               className="btn btn-default",
                                                               style={"margin": "5px"},
                                                               color="primary", 
                                                               disabled=not uploaded), 
															href='/'),
                                                    
                                                    dcc.Link(
														dbc.Button("Clear Data",
                                                               className="btn btn-default",
                                                               style={"margin": "5px"},
                                                               color="primary", 
                                                               disabled=not uploaded), 
															href='/data_import'),
                                                    
                                                    dcc.Link(
														dbc.Button("Data Profling",
                                                               className="btn btn-default",
                                                               style={"margin": "5px"},
                                                               color="primary", 
                                                               disabled=not uploaded), 
															href='/data_profiling'),

                                                    dcc.Link(dbc.Button("Data visualization", 
                                                               className="btn btn-default",
                                                               style={"margin": "5px"},
                                                               color="primary", 
                                                               disabled=not uploaded),
                                                             href='/data_visualization'),

                                                    dcc.Link(
                                                        dbc.Button("Data problems", 
                                                               className="btn btn-default",
                                                               style={"margin": "5px"},
                                                               color="primary", 
                                                               disabled=not uploaded),
                                                            href='/data_problem'),

                                                    dcc.Link(dbc.Button("Data Modelling", 
                                                               className="btn btn-default",
                                                               style={"margin": "5px"},
                                                               color="primary", 
                                                               disabled=not uploaded),
                                                             href="#")

                                         ], style= {"display": "flex", "width": "50%"}
                                    )
                             ], 
    
                )

def load_data_import_page():
    """
    load_data_import_page creates the data import page

    Returns
    -------
    data import page
        Loads the data import page
    """    ""
    return html.Div(
                    id="data-import",
                    children= [learn_more_button(),
                               create_navbar('DATA IMPORT'), 
                               file_upload(), 
                            #    create_next_buttons(),
                               html.Div(id='output-data-profiling')
                               ],
                    )



