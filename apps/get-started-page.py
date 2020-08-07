import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = "Automated Data Science and Machine learning platform"

# make a reuseable navitem for the different examples
version = dbc.NavItem(dbc.NavLink("Version 1.0.0", href="#"))
explore = dbc.NavItem(dbc.NavLink("Explore", href="#"))
get_started = dbc.NavItem(dbc.NavLink("Get started", href="#"))

# make a reuseable dropdown for the different examples
features = dbc.DropdownMenu(
    children=[
                dbc.DropdownMenuItem("Features", header=True),
                dbc.DropdownMenuItem("Data profiling", href="#"),
                dbc.DropdownMenuItem("Detect common data problems", href="#"),
                dbc.DropdownMenuItem("Data visualization", href="#"),
                dbc.DropdownMenuItem("Make a prediction", href="#"),
    ],
    nav=True,
    in_navbar=True,
    label="Learn More",
)

nav_bar = dbc.Navbar(
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
                    [version, explore, get_started, features], 
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

slider = html.Div(className="slider", 
                  children=[html.Span(id="slide-1"), 
                            html.Span(id="slide-2"), 
                            html.Span(id="slide-3"), 
                            html.Span(id="slide-4"), 
                            
                            html.Div(className="image-container", 
                                     children=[html.Img(src="./assets/slider-1.jpg",
                                                        className="slide", 
                                                        width="1650", 
                                                        height="350"), 
                                               
                                               html.Img(src="./assets/slider-2.jpg",
                                                        className="slide",
                                                        width="1650", 
                                                        height="350"), 
                                               
                                               html.Img(src="./assets/slider-3.jpg", 
                                                        className="slide",
                                                        width="1650", 
                                                        height="350"),
                                               
                                               html.Img(src="./assets/slider-4.jpg", 
                                                        className="slide",
                                                        width="1650", 
                                                        height="350")
                                               ],
                                     ),
                            
                            html.Div(className="buttons", 
                                     children=[html.A(href="#slide-1"), 
                                               html.A(href="#slide-2"), 
                                               html.A(href="#slide-3"),
                                               html.A(href="#slide-4")])
                            ]
                  )


features_box = html.Div(id="site-features", 
                 className="features-box",
                 children=[
                     
                     html.A(href="#", 
                            children=[
                                html.Div(
                                    [html.H3("Data Profiling & understanding"),
                                     html.Img(src="/assets/data-profiling.png",
                                              height="95px",
                                              alt="Data profiling and understanding")
                                     ])
                            ],
                            ),

                     html.A(href="#", 
                            children=[
                                html.Div(
                                    [html.H3("Detect problems in your datasets"),
                                     html.Img(src="/assets/data-cleaning.png",
                                              height="55px",
                                              alt="Detect common problems in the dataset")
                                     ])
                            ],
                            ),
                     

                     html.A(href="#", 
                            children=[
                                html.Div(
                                    [html.H3("Data cleaning and wrangling"),
                                     html.Img(src="/assets/data-cleaning.png",
                                              height="55px",
                                              alt="Clean up and get your data in the right shape")
                                     ])
                            ],
                            ),

                     html.A(href="#", 
                            children=[
                                html.Div(
                                    [html.H3("Data Visualization"),
                                     html.Img(src="/assets/data-viz.png",
                                              height="85px",
                                              alt="Build powerful data visualization charts")
                                     ])
                            ],
                            ),
                     
                     html.A(href="#", 
                            children=[
                                html.Div(
                                    [html.H3("Build machine learning models"),
                                     html.Img(src="/assets/machine-learning.png",
                                              height="105px",
                                              alt="Build accurate and predictive models")
                                     ])
                            ],
                            ),
                     
                 ]
                 
                 )


app.layout = html.Div(
    id="get-started-app",
    children= [nav_bar, slider, features_box],

)


if __name__ == '__main__':
    app.run_server(debug=True,
                   use_reloader=False, 
                   port=8080)
    
