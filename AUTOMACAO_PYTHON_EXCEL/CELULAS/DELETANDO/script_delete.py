from openpyxl import load_workbook

nome_arquivo = 'AUTOMACAO_PYTHON_EXCEL\\CELULAS\DELETANDO\\book.xlsx'
wb = load_workbook(filename=nome_arquivo)

ws = wb['Data']
ws.delete_rows(1,3)
ws.delete_cols(1,4)

wb.save(filename=nome_arquivo)