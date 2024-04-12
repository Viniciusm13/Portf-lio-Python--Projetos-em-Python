import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText  # Adicionando a importação necessária
from email import encoders

def enviar_email_com_anexo(para, assunto, mensagem, arquivo_anexo):
    # Configurações de e-mail
    servidor_smtp = 'smtp.example.com'
    porta_smtp = 587  # Usar porta do servidor SMTP
    usuario = 'seu_email@example.com'  # Substituir pelo seu e-mail
    senha = 'senha'  # Substituir pela sua senha

    # Criar uma mensagem multipart
    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = para
    msg['Subject'] = assunto

    # Adicionar corpo da mensagem
    corpo_mensagem = mensagem   # Escreva seu texto do email aqui
    msg.attach(MIMEText(corpo_mensagem, 'plain'))

    # Adicionar anexo
    with open(arquivo_anexo, 'rb') as anexo:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(anexo.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(arquivo_anexo)}')
    msg.attach(part)

    # Enviar e-mail
    servidor = smtplib.SMTP(host=servidor_smtp, port=porta_smtp)
    servidor.starttls()
    servidor.login(usuario, senha)
    servidor.send_message(msg)
    servidor.quit()

# Exemplo parâmetros
para = 'email do destinatário'
assunto = 'Assunto do email'
mensagem = 'Corpo do email'

caminho_arquivo_anexo = r'C:\Users\Exemplo\Desktop\exemplo.xlsx'  # Caminho do arquivo que quer anexar

enviar_email_com_anexo(para, assunto, mensagem, caminho_arquivo_anexo)
