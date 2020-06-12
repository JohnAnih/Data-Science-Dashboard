import json
import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from layouts import page_home, page_404, page_upload, page_dashboard
from src import settings, parser

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.config.suppress_callback_exceptions = True
app.title = settings.APP_NAME
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Loading(type='graph', fullscreen=True, children=[
        dcc.Store(id='data-store')])
])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    """Docstring."""
    if pathname == '/':
        page_content = page_home.layout
    elif pathname == '/upload':
        page_content = page_upload.layout
    elif pathname == '/dashboard':
        page_content = page_dashboard.layout
    else:
        page_content = page_404.layout
    return page_content

@app.callback(
    [Output('url', 'pathname'), Output('data-store', 'data'), Output('modal-upload-option', 'is_open'), Output('alert-upload', 'children'), Output('debug', 'children')],
    [Input('upload-file', 'contents'), Input('upload-option-ok', 'n_clicks'), Input('upload-option-cancel', 'n_clicks')],
    [State('sheet-index', 'value')])
def upload_data(contents, option_ok, option_cancel, sheet_index):
    """Docstring."""
    url, dataset, modal, alert, debug = dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    ctx = dash.callback_context
    content_type, content = contents.split(',')
    if ctx.triggered[0]['prop_id'] == 'upload-file.contents':
        if content_type in settings.FILETYPE['spreadsheet']:
            modal = True
            debug = 'spreadsheet file'
        elif content_type in settings.FILETYPE['csv']:
            status, dataset = parser.parse(content, 'csv')
            url = '/dashboard'
        else:
            alert = dbc.Alert(['Non supported file type'], dismissable=True, color='danger')
    elif ctx.triggered[0]['prop_id'] == 'upload-option-ok.n_clicks':
        status, dataset = parser.parse(content, 'spreadsheet', sheet_index)
        if status == 'wrong_sheet_index':
            alert = dbc.Alert(['Sheet Index not found'], dismissable=True, color='danger')
        else:
            pass
            url = '/dashboard'
        modal = False
    elif ctx.triggered[0]['prop_id'] == 'upload-option-cancel.n_clicks':
        modal = False
    else:
        debug = 'none'
    return url, dataset, modal, alert, debug

@app.callback(
    Output('data-overview', 'children'),
    [Input('trigger-dashboard', 'value')],
    [State('data-store', 'data')])
def show_dashboard(trigger_value, dataset):
    """Docstring."""
    df = pd.read_json(dataset, orient='split')
    output = dash_table.DataTable(id='table_overview', columns=[{'name': col, 'id': col} for col in df.columns], data=df.head(10).to_dict('row'))
    return output


if __name__ == '__main__':
    app.run_server(debug=True)