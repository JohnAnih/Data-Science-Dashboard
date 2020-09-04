import json, math
import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ALL, MATCH
from index import index_layout
from data_import import load_data_import_page
from data_preview import preview_layout
from data_profiling import profiling_layout
from data_problem import dataproblem_layout
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
                              clear_data=True,
                              storage_type='local')])
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    """Docstring."""
    if pathname == '/' or pathname == '/get-started-page':
        return index_layout
    elif pathname == '/data_import':
        return load_data_import_page()
    elif pathname == '/data_preview':
        return preview_layout
    elif pathname == '/data_profiling':
        return profiling_layout
    elif pathname == '/data_problem':
        return dataproblem_layout
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
     Output('url', 'pathname')],
    
    [Input('upload-data', 'contents'), 
     Input('upload-option-ok', 'n_clicks'), 
     Input('upload-option-cancel', 'n_clicks')],
    [State('sheet-index', 'value')])

def upload_data(contents, option_ok, option_cancel, sheet_index):
    """Docstring."""
    datasets, modal, alert, url = dash.no_update, dash.no_update, dash.no_update, dash.no_update
    
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
        url = '/data_preview'
        datasets = json.dumps(datasets)
    
    return datasets, modal, alert, url

def show_preview_data(df):
    return dash_table.DataTable(id='table_overview', 
                                      
                                      columns=[{'name': col, 
                                                'id': col} 
                                               for col in df.columns],
                                      
                                      style_table= {'overflowX': 'auto', 
                                                    'height': '300px', 
                                                    'overflowY': 'auto', 
                                                    "width": "83%",
                                                    "margin-left": "9%"},
                                      
                                      style_data = {"text-align": "center"},
                                      
                                      style_header={
                                          'backgroundColor': 'rgb(6, 67, 122)',
                                          'color': 'white',
                                          "text-align": "center",
                                          'fontWeight': 'bold'},
                                      
                                      style_cell={
                                          # all three widths are needed
                                          'minWidth': '180px', 
                                          'width': '180px', 
                                          'maxWidth': '180px',
                                          'overflow': 'hidden',
                                          'textOverflow': 'ellipsis',
                                        },
                                      
                                      data=df.to_dict('records'),
                                      
<<<<<<< HEAD
                                      page_size=20,
                            
                                      
                                      )
        
        
        datasets = json.dumps(datasets)
    
    return datasets, modal, alert, output
=======
                                      page_size=20)
>>>>>>> c627a5016bd304a0e36f5398f6ec89cf2d06db12

@app.callback(
    Output('output-data-overview', 'children'),
    [Input('trigger-preview', 'value')],
    [State('data-store', 'data')]
)
def show_table(trigger_value, datasets):
    datasets = json.loads(datasets)
    df = pd.read_json(datasets['data'], 
                        orient='split')
    return show_preview_data(df)

def num_format(x):
    return round(x, 2) if isinstance(x, float) and not math.isnan(x) and int(x) != x else x

def check_dtype(df, col, first_dtype):
    if first_dtype == 'float64':
        if df[col].apply(lambda x: True if pd.isna(x) else int(x) == x).all():
            return 'Int64'
    if first_dtype == 'object':
        if df[col].nunique() <= 20 or df[col].nunique() < df.shape[0] * 0.5:
            return 'category'
    return first_dtype

def check_data_problem(df, col, first_dtype):
    problems = []
    true_dtype =  check_dtype(df, col, first_dtype)
    if true_dtype != first_dtype:
        problems.append(f'Wrong datatype, should be {true_dtype}')
    if df.duplicated(col).any():
        problems.append('Found Duplicate value')
    if df[col].isna().any():
        problems.append('Found Missing value')
    if first_dtype in ('float64', 'Int64'):
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        if ((df[col] < (q1 - 1.5*iqr)) | (df[col] > (q3 + 1.5*iqr))).any():
            problems.append('Found Outliers')
    return problems

def check_possible_dtype(df, col, first_dtype):
    dtypes = ['int64', 'float64', 'object', 'category', 'datetime64[ns]']
    possible_dtype = []
    possible_dtype.append(first_dtype)
    for dtype in dtypes:
        if dtype != first_dtype:
            try:
                df[col].astype(dtype)
                possible_dtype.append(dtype)
            except Exception as e:
                pass
    return possible_dtype

def table_info(df, df_profiling, col):
    res = []
    res.append(html.H5(col))
    tbl = []
    for idx in df_profiling.index:
        if not pd.isna(df_profiling.loc[idx, col]):
            if idx == 'dtype':
                first_dtype = df_profiling.loc[idx, col]
                true_dtype = check_dtype(df, col, first_dtype)
                value = first_dtype
            else:
                value = num_format(df_profiling.loc[idx, col])
            tbl.append(html.Tr([html.Td(idx), ' : ', html.Td(value)]))
    res.append(html.Table(tbl))
    return res, first_dtype

def profiling(df, with_problem=False):
    result = []
    df_profiling = parser.data_profiling(df)
    df_profiling.set_index('index', inplace=True)
    for col in df_profiling.columns:
        res, first_dtype = table_info(df, df_profiling, col)
        chart = {
            'data': [{'x': df[col], 'type': 'histogram'}]}
        if with_problem:
            problems = check_data_problem(df, col, first_dtype)
            possible_dtype = check_possible_dtype(df, col, first_dtype)
            right_side = html.Div([
                'Change dtype : ',
                dcc.Dropdown(
                    id={
                        'type': 'change-dtype',
                        'index': list(df.columns).index(col)
                    }, 
                    options=[{'label': dtype, 'value': dtype} for dtype in possible_dtype],
                    placeholder='Change dtype',
                    value=possible_dtype[0]),
                'Data Problems : ',
                html.Ul([html.Li(prob) for prob in problems])],
                style={'width': '30%'}
            )
        else:
            right_side = None
        result.append(dbc.Row([
            html.Div(
                res, 
                id={
                    'type': 'change-dtype-output',
                    'index': list(df.columns).index(col)
                }), 
            dcc.Graph(figure=chart), right_side]))
    return result

@app.callback(
    Output('output-data-profiling', 'children'),
    [Input('trigger-profiling', 'value')],
    [State('data-store', 'data')]
)
def show_data_profiling(value, datasets):
    datasets = json.loads(datasets)
    df = pd.read_json(datasets['data'], orient='split')
    table_overview, table_profiling = dash.no_update, dash.no_update
    return html.Div([
        html.H3('Data Profiling'),
        dbc.Col(profiling(df), style={'margin': '20px'})
    ])


@app.callback(
    Output('output-data-problem', 'children'),
    [Input('trigger-problem', 'value')],
    [State('data-store', 'data')]
)
def show_data_profiling(value, datasets):
	datasets = json.loads(datasets)
	df = pd.read_json(datasets['data'], orient='split')
	table_overview, table_dataproblem = dash.no_update, dash.no_update
	return html.Div([
		html.H3('Data Problems'),
		dbc.Col(profiling(df, with_problem=True), style={'margin': '20px'})
	])

@app.callback(
    Output({'type': 'change-dtype-output', 'index': MATCH}, 'children'),
    [Input({'type': 'change-dtype', 'index': MATCH}, 'value')],
    [State({'type': 'change-dtype', 'index': MATCH}, 'id'),
     State('data-store', 'data')],
)
def display_output(value, id, datasets):
    datasets = json.loads(datasets)
    df = pd.read_json(datasets['data'], orient='split')
    col = df.columns[int(id['index'])]
    df[col] = df[col].astype(value)
    df_profiling = parser.data_profiling(df)
    df_profiling.set_index('index', inplace=True)
    res, first_dtype = table_info(df, df_profiling, col)
    return res

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