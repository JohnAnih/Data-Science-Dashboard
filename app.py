import json, math
import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from layouts import page_home, page_404, page_upload, page_feature, page_data_profiling
from src import settings, parser
import matplotlib.pyplot as plt
import missingno as msno
from plotly.tools import mpl_to_plotly

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.config.suppress_callback_exceptions = True
app.title = settings.APP_NAME
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Loading(type='graph', fullscreen=True, children=[
        dcc.Store(id='data-store', storage_type='local')])
])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    """Docstring."""
    if pathname == '/':
        page_content = page_home.Build_home_page()
    elif pathname == '/upload':
        page_content = page_upload.layout
    elif pathname == '/feature':
        page_content = page_feature.layout
    elif pathname == '/data_profiling':
        page_content = page_data_profiling.layout
    else:
        page_content = page_404.layout
    return page_content

@app.callback(
    [Output('url', 'pathname'), Output('data-store', 'data'), Output('modal-upload-option', 'is_open'), Output('alert-upload', 'children'), Output('debug', 'children')],
    [Input('upload-file', 'contents'), Input('upload-option-ok', 'n_clicks'), Input('upload-option-cancel', 'n_clicks')],
    [State('sheet-index', 'value')])
def upload_data(contents, option_ok, option_cancel, sheet_index):
    """Docstring."""
    url, datasets, modal, alert, debug = dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    ctx = dash.callback_context
    content_type, content = contents.split(',')
    if ctx.triggered[0]['prop_id'] == 'upload-file.contents':
        if content_type in settings.FILETYPE['spreadsheet']:
            modal = True
            debug = 'spreadsheet file'
        elif content_type in settings.FILETYPE['csv']:
            status, datasets = parser.parse(content, 'csv')
            url = '/feature'
        else:
            alert = dbc.Alert(['Non supported file type'], dismissable=True, color='danger')
    elif ctx.triggered[0]['prop_id'] == 'upload-option-ok.n_clicks':
        status, datasets = parser.parse(content, 'spreadsheet', sheet_index)
        if status == 'wrong_sheet_index':
            alert = dbc.Alert(['Sheet Index not found'], dismissable=True, color='danger')
        else:
            pass
            url = '/feature'
        modal = False
    elif ctx.triggered[0]['prop_id'] == 'upload-option-cancel.n_clicks':
        modal = False
    else:
        debug = 'none'
    return url, datasets, modal, alert, debug

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
    Output('data-overview', 'children'),
    [Input('trigger-dashboard', 'value')],
    [State('data-store', 'data')])
def show_dashboard(trigger_value, datasets):
    """Docstring."""
    datasets = json.loads(datasets)
    df = pd.read_json(datasets['data'], orient='split')
    ax = msno.matrix(df)
    fig = ax.get_figure()
    plotly_fig = mpl_to_plotly(fig)
    table_overview, table_profiling = dash.no_update, dash.no_update
    return html.Div([
        html.H3('First 5 rows'),
        html.Div(dash_table.DataTable(id='table_overview', columns=[{'name': col, 'id': col} for col in df.columns], data=df.head(5).to_dict('row'), style_cell={'width': 'auto'}), style={'margin': '40px'}),
        html.Br(),
        #  dcc.Graph(figure=plotly_fig),
        html.H3('Data Profiling'),
		dbc.Col(profiling(df), style={'margin': '20px'})
    ])



if __name__ == '__main__':
    app.run_server(debug=True)