from layouts.import_libs import *
import data_import
from layouts.page_home import create_footer

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
    authors = html.A(dbc.NavItem(dbc.NavLink("Meet the Team")), href="#meet-the-team")
    explore = html.A(dbc.NavItem(dbc.NavLink("Explore")), href="#explore-features")
    get_started = dbc.NavItem(dbc.NavLink("Get started", href="/data_import"))

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
                            href="/",
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
                        style={'font-size': '14px'},
                        className="card-text",
                    ),

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
                        style={'font-size': '14px'},
                        className="card-text",
                    ),
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
                    style={'font-size': '14px'},
                    className="card-text",
                ),
            ], 
        ),
    ]

    data_viz = [
        dbc.CardImg(src="../assets/icons/png/Data visualization_icon.png", top=True),
        dbc.CardBody(
            [
                html.H5("Data visualization", className="card-title"),
                html.P(
                    "Visualize your data to get insghts from the data",
                    style={'font-size': '14px'},
                    className="card-text",
                ),
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
                    style={'font-size': '14px'},
                    className="card-text",
                ),
            ], 
        ),
    ]
    
    return html.Div(
        
        id= "explore-features",
        
        children=   [
                        html.H1("Features", 
                                style={"color": "rgb(6, 67, 122)", 
                                       "font-size": "60px",
                                       "text-align": "center"}
                                ),
                        
                        html.Div(
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

                                
                                ),
                                
                                html.H1("Get Started", 
                                        style={'color': 'white', 
                                               'text-align': 'center', 
                                               'padding-top': '1%'}),
                                
                                html.P("You can get started here by uploading your dataset", 
                                       style={'color': 'white', 
                                              'text-align': 'center', 
                                              'font-size': '14px'}), 
                                
                                html.P("Very easy to use, no need for any guide or documentation, just click the Get started button", 
                                       style={'color': 'white', 
                                              'text-align': 'center', 
                                              'font-size': '14px', 
                                              'padding-bottom': '3%'}), 
                                
                                dcc.Link(dbc.Button("Get started", 
                                                    color="danger", 
                                                    style={'width': '20%', 
                                                           'padding': '1%', 
                                                           'margin-left': '39%'}), 
                                         href="/data_import", 
                                         
                                         style={"color":"white", 
                                                "text-decoration":"none"}),
                                
               

                        ],
                            style={"background-color": "rgb(6, 67, 122)", 
                                   "padding-top": "2%", 
                                   "padding-bottom": "4%", 
                                   "padding-left": "10%",
                                   "padding-right": "10%"}
                    ),
                        


                    ], 

            style={"margin-top": "2%", 
                   "text-align": "left"}
        )


def meet_the_team():
    

    johnanih = dbc.Card(
            dbc.CardBody(
                [
        
                    html.Img(src="../assets/images/johnanih.png", 
                    alt="John Anih", 
                    style={"width": "60%"}),
                    
                    html.H5("John Anih", className="card-title"),
            
                    dcc.Markdown(
                        """ 
                        <b> Data Scientist/ Python developer </b>
                        
                        <p> Founder/ CEO </p>
                        
                        
                        """,
                        dangerously_allow_html=True,
                        className="card-text",
                        
                    ),
            
                    dbc.Button(
                        "Contact me", 
                        color="success", 
                        className="mt-auto", 
                        href="mailto:tj.anih@gmail.com"
                    ),
                    
                    
                ]
            ), style= {"border": "solid 5px rgb(6, 67, 122)"}
        ),
        
    irfan = dbc.Card(
            dbc.CardBody(
                [
        
                    html.Img(src="../assets/images/irfan-chi.png", 
                    alt="Irfan Chahyadi", 
                    style={"width": "56%"}),
                    
                    html.H5("Irfan Chahyadi", className="card-title"),
            
                    dcc.Markdown(
                        """ 
                        <b> Data Scientist/ Python developer </b>
                        
                        <p> Co-Founder/ Contributor </p>
                        
                        
                        """,
                        dangerously_allow_html=True,
                        className="card-text",
                        
                    ),
            
                    dbc.Button(
                        "Contact me", 
                        color="success", 
                        className="mt-auto", 
                        href="mailto:Irfanchahyadi@gmail.com"
                    ),
                    
                    
                ]
            ), style= {"border": "solid 5px rgb(6, 67, 122)"}
        ),
    
    team_cards = dbc.Row([dbc.Col(johnanih, width=6), dbc.Col(irfan, width=6)])
        
    return html.Div(
        
        id= "meet-the-team",
        
        style={"margin-left": "25%", 
               "margin-right": "25%", 
               "padding-bottom": "10%", 
               "padding-top": "2%", 
               "width": "50%"},
        children= [
            html.H1("Meet the team", 
                    
                    style={"color": "rgb(6, 67, 122)", 
                           "font-size": "60px",
                           "text-align": "center",
                           
                           }),
            
            html.Br(),
            team_cards,
                    ]
        )



index_layout = html.Div(
    id="get-started-app",
    
    children= [create_navbar(), 
               create_image_slider(), 
               display_features_using_cards(), 
               meet_the_team(), 
               create_footer()],

)

