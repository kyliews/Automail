import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

def search_db():
    df = pd.read_excel(r'*your path*\Automail\src\enterprises.xlsx')
    destinatarios = df["Destinatarios"].tolist()  # Convertendo para uma lista de destinatários
    return destinatarios

# Tokens
host = "smtp-mail.outlook.com"
port = 587
login = "*email you use*"
senha = "**"

message = MIMEMultipart("alternative")
message['Subject'] = "CV - Analista de Dados"

# Lendo o conteúdo do arquivo HTML
with open(r"*your path*\Automail\front\template.html", "r", encoding="utf-8") as file:
    html = file.read()

html_part = MIMEText(html, 'html')
message.attach(html_part)

destiny = search_db()

message['From'] = login
message['Cc'] = login
message['Bcc'] = login

smtp = smtplib.SMTP(host, port)

status_code, response = smtp.ehlo()
print(f"[] Echoing server: {status_code}{response}")

status_code, response = smtp.starttls()
print(f"[] Echoing TLS connection: {status_code}{response}")

status_code, response = smtp.login(login, senha)
print(f"[*] Login in: {status_code}{response}")

for destinatario in destiny:
    message['To'] = destinatario
    smtp.sendmail(login, destinatario, message.as_string())
    print(f"Enviado para:{destinatario}")
    sleep(60)  # Aguarda 10 segundos entre o envio de cada email

smtp.quit()