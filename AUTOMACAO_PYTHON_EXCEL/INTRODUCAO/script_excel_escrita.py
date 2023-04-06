from openpyxl import Workbook

wb = Workbook()

arquivo = 'AUTOMACAO_PYTHON_EXCEL\\INTRODUCAO\\primeiro_arquivo.xlsx'

ws1 = wb.active
ws1.title = 'Planilha 1'

dados = [
    
    ['Ano', 'Lucro', 'Custos'],
    [2015, '30%', '40%'],
    [2016, '10%', '45%'],
    [2017, '45%', '40%'],
    
]


for linha in dados:
    ws1.append(linha)
    
ws2 = wb.create_sheet(title='Planilha 2')
ws2['F5'] = 3.14
    
wb.save(filename=arquivo)