import base64, io
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
        dataset = df.to_json(date_format='iso', orient='split')
        status = 'success'
    except IndexError:
        dataset = None
        status = 'wrong_sheet_index'
    return status, dataset