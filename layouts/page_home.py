import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    'Landing Page',
    html.Div([
        dcc.Link('Getting Started', href='/upload')
    ])
])

def Build_home_page():
    """
    build_welcome_banner creates the get started page.

    Returns
    -------
    Rendered Dash HTML
    """    ""
    
    return html.Div( id="flex-page", 
                    children=[
                        html.Div(
                                id="banner",
                                children= html.Div(
                                        id="welcome-user",
                                        children=[
                                            html.H1("WELCOME TO THE DATA SCIENCE"),
                                            html.H1("AND MACHINE LEARNING PLATFORM"),
                                            html.Hr(className="tickline"),
                                            html.Br(),
                                            html.P(id="welcome-text1",
                                                   children= "That provides you with the tools that allow you to explore your data seemlessly and"
                                                       ),
                                            html.P(id= "welcome-text2",
                                                   children= "get actionable insights from your data and allows you to easily apply Machine learning models to make predictions with your data"
                                                       ),
                                                    ],
                                            ),
                                ),  

                            html.Div(
                                 id="feature-zone",
                                 children= [
                                        html.Br(),
                                        html.H1(id="featurestext",
                                                   children="Features"),
                                        html.Br(),
                                            ]

                            ),

                            html.Div(
                                 id="Boxes-for-features",
                                 className= "flex-features",
                                 children= [
                                        html.Br(),

                                        html.A([
                                            html.H1("DATA COLLECTION AND SURVEY"), 
                                            html.Div("Create a survey to get the data and perform necessary data preparations"),
                                            ], 
                                            href="https://dash.plotly.com/layout"),                        

                                        html.A([
                                            html.H1("DATA PROFILING AND UNDERSTANDING"), 
                                            html.Div("If you have your data. You can easily profile your data and get insights about your data, detect common problems with your data and get it cleaned"),
                                            ], 
                                            href="https://dash.plotly.com/layout"),

                                         html.A([
                                            html.H1("DATA VISUALIZATION"), 
                                            html.Div("visualize your data and get insights about your data"),
                                            ], 
                                            href="https://dash.plotly.com/layout"),                       

                                        html.A([
                                            html.H1("MACHINE LEARNING"), 
                                            html.Div("Make predictions with your data"),
                                            ], 
                                            href="https://dash.plotly.com/layout"),
                                            ]

                            ),
                            
                            html.Div(
                                 id="call-to-action",
                                 
                                 children= [
									 	dcc.Link('Find Out More', href='/upload'),
                                        # html.A("Find Out More", href="https://dash.plotly.com/layout"),
                                        html.Br(),
                                            ]

                            ),
                        ],
    )