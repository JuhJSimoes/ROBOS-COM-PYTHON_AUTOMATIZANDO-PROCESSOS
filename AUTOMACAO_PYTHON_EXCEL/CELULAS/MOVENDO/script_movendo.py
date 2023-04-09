from openpyxl import load_workbook

dest_filename = 'AUTOMACAO_PYTHON_EXCEL\\CELULAS\\MOVENDO\\book.xlsx'

wb = load_workbook(filename=dest_filename)
ws = wb['Data']


#Move da linha 2 de A2 ate Z2 uma linha pra cima
ws.move_range('A2:Z2', rows=-1)

#Move coluna
ws.move_range('F8', cols=2)
ws.move_range('F10', cols=-2)

ws.move_range('C13:E15', cols=-2, rows=-1)

wb.save(dest_filename)