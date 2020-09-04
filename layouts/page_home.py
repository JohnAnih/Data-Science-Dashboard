import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_trich_components as dtc

def create_footer():
    """
    create_footer creates the footer for the website

    Returns
    -------
    Footer
    """    ""
    
    footer_styles = {"display": "inline", 
                     "padding-left": "35px",
                     "padding-right": "35px", 
                     "margin-top": "40px"}
    
    return html.Div(className="footer",
                    children=[
                        html.Div("Copyright © ADSML, 2020", style=footer_styles),
                        
                        html.Div(
                            children=[html.A("Visit our blog", 
                                             href="#", 
                                             style={"color":"white", "text-decoration":"none"}
                                             )
                                      ], 
                            style=footer_styles),
                        
                        html.Div(
                            children=[html.A("Future updates", 
                                             href="#", 
                                             style={"color":"white", "text-decoration":"none"}
                                             )
                                      ], 
                            style=footer_styles),
                        ]
                    )