import json, math
import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from  index import index_layout
from data_import import load_data_import_page
from src import settings, parser



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
        return load_data_import_page()
    # elif pathname == '/feature':
    #     page_content = page_feature.layout
    # elif pathname == '/data_profiling':
    #     page_content = page_data_profiling.layout
    # else:
    #     page_content = page_404.layout
    #return page_content

@app.callback(
    Output("data-import-learn-more-button", "is_open"),
    
    [Input("learn-more-button", "n_clicks"), 
     Input("learn-more-close-button-data-import", "n_clicks")],
    
    [State("data-import-learn-more-button", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    [Output('data-store', 'data'), 
     Output('modal-upload-option', 'is_open'), 
     Output('alert-upload', 'children'), 
     Output('output-data-upload', 'children')],
    
    [Input('upload-data', 'contents'), 
     Input('upload-option-ok', 'n_clicks'), 
     Input('upload-option-cancel', 'n_clicks')],
    [State('sheet-index', 'value')])

def upload_data(contents, option_ok, option_cancel, sheet_index):
    """Docstring."""
    datasets, modal, alert, output = dash.no_update, dash.no_update, dash.no_update, dash.no_update
    
    ctx = dash.callback_context
    
    if contents:
        #content_type, content = contents.split(',')
        
        if ctx.triggered[0]['prop_id'] == 'upload-data.contents':

            if contents.split(',')[0] in settings.FILETYPE['spreadsheet']:
                modal = True

            elif contents.split(',')[0] in settings.FILETYPE['csv']:
                status, datasets = parser.parse(contents.split(',')[1], 'csv')

            else:
                alert = dbc.Alert(['Non supported file type'], 
                                  dismissable=True, 
                                  color='danger')
    
        elif ctx.triggered[0]['prop_id'] == 'upload-option-ok.n_clicks':

            status, datasets = parser.parse(contents.split(',')[1], 
                                            'spreadsheet', 
                                            sheet_index)

            if status == 'wrong_sheet_index':
                alert = dbc.Alert(['Sheet Index not found'], 
                                  dismissable=True, 
                                  color='danger')
            else:
                pass
            modal = False

        elif ctx.triggered[0]['prop_id'] == 'upload-option-cancel.n_clicks':
            modal = False
    
    if isinstance(datasets, dict):
        df = pd.read_json(datasets['data'], 
                          orient='split')
        
        output = dash_table.DataTable(id='table_overview', 
                                      
                                      columns=[{'name': col, 
                                                'id': col} 
                                               for col in df.columns], 
                                      
                                      data=df.head(5).to_dict('row'))
        
        datasets = json.dumps(datasets)
    
    return datasets, modal, alert, output


def num_format(x):
    return round(x, 2) if isinstance(x, float) and not math.isnan(x) and int(x) != x else x

def check_dtype(df, col, first_dtype):
    if first_dtype == 'float64':
        if df[col].apply(lambda x: True if pd.isna(x) else int(x) == x).all():
            return 'Int64'
    if first_dtype == 'object':
        if df[col].nunique() <= 20 or df[col].nunique() < df.shape[0] * 0.5:
            return 'category'
    else:
        return first_dtype

def profiling(df):
    df_profiling = parser.data_profiling(df)
    result = []
    df_profiling.set_index('index', inplace=True)
    for col in df_profiling.columns:
        res = []
        res.append(html.H5(col))
        tbl = []
        for idx in df_profiling.index:
            if not pd.isna(df_profiling.loc[idx, col]):
                if idx == 'dtype':
                    first_dtype = df_profiling.loc[idx, col]
                    true_dtype = check_dtype(df, col, first_dtype)
                    if first_dtype == true_dtype:
                        value = first_dtype
                    else:
                        value = [first_dtype, dbc.Button('change to ' + true_dtype, style={'margin-left': '10px'})]
                else:
                    value = num_format(df_profiling.loc[idx, col])
                tbl.append(html.Tr([html.Td(idx), ' : ', html.Td(value)]))
        res.append(html.Table(tbl))
        chart = {
            'data': [{'x': df[col], 'type': 'histogram'}]
        }
        result.append(dbc.Row([html.Div(res), dcc.Graph(figure=chart)]))
    return result


@app.callback(
    Output('output-data-profiling', 'children'),
    [Input('show-data-profiling', 'n_clicks')],
    [State('data-store', 'data')]
)
def show_data_profiling(click, datasets):
    if click:
        datasets = json.loads(datasets)
        df = pd.read_json(datasets['data'], orient='split')
        table_overview, table_profiling = dash.no_update, dash.no_update
        return html.Div([
            html.H3('Data Profiling'),
            dbc.Col(profiling(df), style={'margin': '20px'})
        ])
    return ''

# @app.callback(Output('output-data-upload', 'children'),
#               [Input('upload-data', 'contents')],
#               [State('upload-data', 'filename'),
#                State('upload-data', 'last_modified')])
# def update_output(list_of_contents, list_of_names, list_of_dates):
#     if list_of_contents is not None:
#         children = [
#             parse_contents(c, n, d) for c, n, d in
#             zip(list_of_contents, list_of_names, list_of_dates)]
#         return children

if __name__ == '__main__':
    app.run_server(debug=True,
                   use_reloader=False, 
                   port=8080)