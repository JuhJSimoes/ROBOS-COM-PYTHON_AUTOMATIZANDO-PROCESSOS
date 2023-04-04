import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = 'juhsimoesdevrpa@gmail.com'
toaddr = 'juhsimoesdevrpa@gmail.com, julianajsimoes@gmail.com, juliana.simoes@g.globo'

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'E-mail de teste com Selenium'

body = 'E-mail automático enviado pelo robô'

msg.attach(MIMEText(body, 'plain'))

#Servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)

#Segurança
s.starttls()

s.login(fromaddr, 'wsdwwlwkvwkvlwcy')

#Converte para String
text = msg.as_string

s.sendmail(fromaddr, toaddr, text)

s.quit()