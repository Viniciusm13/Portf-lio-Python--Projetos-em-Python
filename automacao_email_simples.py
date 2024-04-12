#   EMAIL SIMPLES, APENAS TEXTO

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(para, assunto, mensagem):
    servidor_smtp = 'smtp.example.com'
    porta_smtp = 587  # Usar porta do servidor SMTP
    usuario = 'seu_email@example.com'  # Substituir pelo seu e-mail
    senha = 'senha'  # Substituir pela sua senha

    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = para
    msg['Subject'] = assunto

    corpo_mensagem = mensagem
    msg.attach(MIMEText(corpo_mensagem, 'plain'))

    servidor = smtplib.SMTP(host=servidor_smtp, port=porta_smtp)
    servidor.starttls()
    servidor.login(usuario, senha)

    servidor.send_message(msg)
    servidor.quit()

# Exemplo parâmetros

para = 'email do destinatário'
assunto = 'Assunto do email'
mensagem = 'Corpo do email'

enviar_email(para, assunto, mensagem)
