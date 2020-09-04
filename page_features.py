from layouts.import_libs import *
from layouts.page_home import create_footer

app = dash.Dash(__name__,
                external_stylesheets = [dbc.themes.BOOTSTRAP])

app.title = "Automated Data Science and Machine learning platform"

def create_navbar():
    """
    create_navbar creates the website Navbar using bootsraps components

    To learn more visit: https://dash-bootstrap-components.opensource.faculty.ai/docs/

    Returns
    -------
    NavBar
        creates the website navrbar
    """    ""
    
    
    title = html.H2("""
                         FEATURE PAGE 
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
                            href="/",
                        ),
                        dbc.NavbarToggler(id="navbar-toggler2"),

                        dbc.Collapse(
                            dbc.Nav(
                                title, 
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
    



def render_tabs():
    tab_style = {
        'borderBottom': '1px solid #d6d6d6',
        'padding': '30px',
        'fontWeight': 'bold'
        }

    tab_selected_style = {
        'borderTop': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'backgroundColor': 'rgb(6, 67, 122)',
        'color': 'white',
        'padding': '30px',
        'margin': '0'
    }
    
    return html.Div(
             
                      [dcc.Tabs(id="feature-tabs", 
                                value='Data Profiling', 
                                
                                children=[
                                           dcc.Tab(label='Data Profiling', 
                                                   value='data-profiling-tab', 
                                                   style=tab_style, 
                                                   selected_style=tab_selected_style),
                                           
                                           dcc.Tab(label='Data Problems', 
                                                   value='data-problems-tab', 
                                                   style=tab_style, 
                                                   selected_style=tab_selected_style),
                                           
                                           dcc.Tab(label='Data Visualization', 
                                                   value='data-visual-tab', 
                                                   style=tab_style, 
                                                   selected_style=tab_selected_style),
                                           
                                           dcc.Tab(label='Machine learning', 
                                                   value='machine-learning-tab', 
                                                   style=tab_style, 
                                                   selected_style=tab_selected_style),
                                           ], 
                                style={'height': '100px'},
                                ),

                       html.Div(id='feature-contents', 
                                style={'margin-left': '10%', 
                                       'padding-top': '4%'})]
                    )

app.layout = html.Div(
    id ="features-page",
    children=[create_navbar(),
              render_tabs(),
              create_footer()]
)

@app.callback(Output('feature-contents', 'children'),
              [Input('feature-tabs', 'value')])
def render_content(tab):
    if tab == "data-profiling-tab":
        return html.Div([
            html.H3('Data Profiling')
        ])
    elif tab == "data-problems-tab":
        return html.Div([
            html.H3('Common Problems in your data')
        ])
    elif tab == "data-visual-tab":
        return html.Div([
            html.H3('Data Visualization')
        ])
    elif tab == "machine-learning-tab":
        return html.Div([
            html.H3('Welcome to the machine learning tab'),
            html.P("Work in progress")
        ])



if __name__ == '__main__':
    app.run_server(debug=True,
                   use_reloader=False, 
                   port=8080)