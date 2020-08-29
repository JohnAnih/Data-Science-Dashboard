import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_trich_components as dtc

import data_import

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
    authors = dbc.NavItem(dbc.NavLink("Meet the Team", href="#"))
    explore = dbc.NavItem(dbc.NavLink("Explore", href="#"))
    get_started = dbc.NavItem(dbc.NavLink("Get started", href="#"))

    # features drop down
    features = dbc.DropdownMenu(
                    children=[
                                dbc.DropdownMenuItem("Features", header=True),
                                dbc.DropdownMenuItem("Data profiling", href="#"),
                                dbc.DropdownMenuItem("Detect common data problems", href="#"),
                                dbc.DropdownMenuItem("Data visualization", href="#"),
                                dbc.DropdownMenuItem("Make a prediction", href="#"),
                                dbc.DropdownMenuItem("Future updates", href="#"),
                                dbc.DropdownMenuItem("Visit our blog", href="#"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Learn More",
               )
    
    return dbc.Navbar(
                dbc.Container(
                    [
                        html.A(
                            # Use row and col to control vertical alignment of logo / brand
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
                                [authors, explore, get_started, features], 
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


def create_image_slider():
    """
    create_image_slider creates the image slider

    Using the Dash trich components.
    
    Learn more here: https://romanonatacha.github.io/dash_trich_components/

    Returns
    -------
    creates the image slider
    """    "" 
    return dtc.Carousel([
           	html.Img(src="../assets/images/Img-%s.jpg" % (numb), 
                     height=300) 
                     for numb in range(1,11)],
                        
            slides_to_scroll=6,
            slides_to_show=1,
            swipe_to_slide=True,
            autoplay=True,
            speed=2000,
            variable_width=True,
            center_mode=True,
            style={"margin-top":"1px"},
            responsive=[
            {
                'breakpoint': 991,
                'settings': {
                    'arrows': True
                }
            }]
		)


def display_features_using_cards():
    """
    display_features_using_cards uses the boostraps cards to display the website features

    To learn more visit: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/

    Returns
    -------
    creates cards representing each feature 
    """    ""
    
    data_import = [
            dbc.CardImg(src="../assets/icons/png/Data import_icon.png", top=True),
            dbc.CardBody(
                [
                    html.H5("Data Import", className="card-title"),
                    html.P(
                        "Upload your data.",
                        className="card-text",
                    ),
                    dbc.Button(dcc.Link("Get started",
                                      href="/data_import",
                           style={"color":"white", "text-decoration":"none"}), 
                           color="primary"),
                ], 
            ), 
       ]
    
    data_profile = [
            dbc.CardImg(src="../assets/icons/png/Data profiling_icon.png", top=True),
            dbc.CardBody(
                [
                    html.H5("Data profiling", className="card-title"),
                    html.P(
                        "Profile your data to get insights",
                        className="card-text",
                    ),
                    dbc.Button(html.A("Get started",
                                      href="#",
                           style={"color":"white", "text-decoration":"none"}), 
                           color="primary"),
                ], 
            ),
        ]

    data_clean = [
        dbc.CardImg(src="../assets/icons/png/Fix data_icon.png", top=True),
        dbc.CardBody(
            [
                html.H5("Data cleaning", className="card-title"),
                html.P(
                    "Detect common problems in your datasets",
                    className="card-text",
                ),
                dbc.Button(html.A("Get started",
                                  href="#",
                           style={"color":"white", "text-decoration":"none"}), 
                           color="primary"),
            ], 
        ),
    ]

    data_viz = [
        dbc.CardImg(src="../assets/icons/png/Data visualization_icon.png", top=True),
        dbc.CardBody(
            [
                html.H5("Data visualization", className="card-title"),
                html.P(
                    "Visualize your data to understand the distribution and get insghts",
                    className="card-text",
                ),
                dbc.Button(html.A("Get started",
                                  href="#",
                           style={"color":"white", "text-decoration":"none"}), 
                           color="primary"),
            ],
        ),
    ]

    data_modeling = [
        dbc.CardImg(src="../assets/icons/png/Data modeling_icon.png", top=True),
        dbc.CardBody(
            [
                html.H5("Machine learning", className="card-title"),
                html.P(
                    "Build a machine learning model",
                    className="card-text",
                ),
                dbc.Button(html.A("Get started",
                                  href="#",
                           style={"color":"white", "text-decoration":"none"}), 
                           color="primary"),
            ], 
        ),
    ]
    
    return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(dbc.Card(data_import, color="light", inverse=True)),
                        dbc.Col(dbc.Card(data_profile, color="light", inverse=True)),
                        dbc.Col(dbc.Card(data_clean, color="light", inverse=True)),
                        dbc.Col(dbc.Card(data_viz, color="light", inverse=True)),
                        dbc.Col(dbc.Card(data_modeling, color="light", inverse=True)),
                    ],
                    className="mb-4",
                    style={"background-color": "rgb(6, 67, 122)", 
                           "padding-top": "2%", 
                           "padding-bottom": "1%", 
                           "padding-left": "2%",
                           "padding-right": "2%"}
                ),
                

            ], 

            style={"margin-top": "2%", 
                   "text-align": "left"}
        )



index_layout = html.Div(
    id="get-started-app",
    
    children= [create_navbar(), 
               create_image_slider(), 
               display_features_using_cards()],

)

