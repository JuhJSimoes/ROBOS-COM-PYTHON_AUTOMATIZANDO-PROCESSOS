from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

ws['A1'] = 'Você verá uma imagem abaixo'

img = Image('AUTOMACAO_PYTHON_EXCEL\\INSERINDO_IMAGENS\\logo.jpg')
ws.add_image(img, 'A3')

wb.save('AUTOMACAO_PYTHON_EXCEL\\INSERINDO_IMAGENS\\logo.xlsx')