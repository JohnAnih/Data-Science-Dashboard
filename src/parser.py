import base64, io, json
import pandas as pd

def parse(content, file_type, sheet_index=None):
    """Docstring."""
    try:
        content_decoded = base64.b64decode(content)
        if file_type == 'csv':
            data = io.StringIO(content_decoded.decode('utf-8'))
            df = pd.read_csv(data)
        elif file_type == 'spreadsheet':
            data = io.BytesIO(content_decoded)
            df = pd.read_excel(data, sheet_name=sheet_index)
        datasets = {
            'data': df.to_json(date_format='iso', orient='split'),
            'profiling': data_profiling(df).to_json(date_format='iso', orient='split')
        }
        status = 'success'
    except IndexError:
        datasets = None
        status = 'wrong_sheet_index'
    return status, json.dumps(datasets)

def data_profiling(df):
    df_profiling = pd.DataFrame({
        'dtype': df.dtypes.astype(str),
        'count': df.count(),
        'unique': df.nunique(),
        'sum': df.sum(numeric_only=True),
        'mean': df.mean(numeric_only=True),
        'std': df.std(numeric_only=True),
        'min': df.min(numeric_only=True),
        'max': df.max(numeric_only=True)
        }).T.reset_index()
    return df_profiling.reindex(columns=['index'] + df.columns.tolist())