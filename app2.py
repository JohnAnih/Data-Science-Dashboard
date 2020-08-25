import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from  index import index_layout
from data_import import data_import_page



app = dash.Dash(__name__,
                external_stylesheets = [dbc.themes.BOOTSTRAP])

app.title = "Automated Data Science and Machine learning platform"

# allow ids from other layouts
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', 
                 refresh=False),
    
    html.Div(id='page-content'),
    
    dcc.Loading(type='graph', 
                fullscreen=True, 
                
                children=[
                    dcc.Store(id='data-store', 
                              storage_type='local')])
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    """Docstring."""
    if pathname == '/':
        return index_layout
    elif pathname == '/data_import':
        return data_import_page
    # elif pathname == '/feature':
    #     page_content = page_feature.layout
    # elif pathname == '/data_profiling':
    #     page_content = page_data_profiling.layout
    # else:
    #     page_content = page_404.layout
    #return page_content

@app.callback(
    Output("data-import-learn-more-button", "is_open"),
    [Input("learn-more-button", "n_clicks"), Input("learn-more-close-button-data-import", "n_clicks")],
    [State("data-import-learn-more-button", "is_open")],
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