from openpyxl import Workbook

print('\nINICIANDO EXECUÇÃO DO ROBÔ\n')
print('Lendo dados do arquivo\n')

file_txt = open('AUTOMACAO_PYTHON_EXCEL\\ROBO_DESPESAS\\gastos.txt', 'r', encoding='utf-8')

arquivo = file_txt.read()

lista_dados = arquivo.splitlines()

print(lista_dados)

print('\nCriando arquivo Excel\n')
for i in range (0, len(lista_dados)):
    lista_dados[i] = lista_dados[i].split(',')

wb = Workbook()
ws = wb.active

for row in lista_dados:
    ws.append(row)

wb.save('AUTOMACAO_PYTHON_EXCEL\\ROBO_DESPESAS\\gastos.xlsx')