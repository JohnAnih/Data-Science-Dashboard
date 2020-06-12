APP_NAME = 'Data-Science Dashboard'

FILETYPE = {
    'spreadsheet': [
        'data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64', # XLSX file
        # 'data:application/vnd.ms-excel;base64', # XLS file
        'data:application/vnd.ms-excel.sheet.macroEnabled.12;base64', # XLSM file
        'data:application/octet-stream;base64' # ET file
    ], 
    'csv': [
        'data:application/vnd.ms-excel;base64', # CSV file
    ] 
}