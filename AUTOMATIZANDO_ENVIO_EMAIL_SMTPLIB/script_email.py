import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = 'juhsimoesdevrpa@gmail.com'
toaddr = 'julianajsimoes@gmail.com'

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'E-mail Srta. Robô'

body = """E-mail automático enviado pelo robô"""

msg.attach(MIMEText(body, 'plain'))


#Anexo
filename = 'AUTOMACAO_PYTHON_SELENIUM\\AUTOMATIZANDO_ENVIO_EMAIL_SMTPLIB\\Srta_Bot.pdf'
anexo = open('AUTOMACAO_PYTHON_SELENIUM\\AUTOMATIZANDO_ENVIO_EMAIL_SMTPLIB\\Srta_Bot.pdf', 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload((anexo).read())

#Enconde base 64
encoders.encode_base64(p)

p.add_header('Content-Disposition', 'attachment; filename= %s' %filename)

msg.attach(p)


#Servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)

#Segurança
s.starttls()

s.login(fromaddr, 'wsdwwlwkvwkvlwcy')

#Converte para String
text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()