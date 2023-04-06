import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from script_email_body import body_email

fromaddr = 'juhsimoesdevrpa@gmail.com'
toaddr = 'julianajsimoes@gmail.com'

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Analista RPA - Envio Aumomático'

part1=MIMEText(body_email, 'html')
msg.attach(part1)

#Servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)

#Segurança
s.starttls()

s.login(fromaddr, 'wsdwwlwkvwkvlwcy')

#Converte para String
text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()