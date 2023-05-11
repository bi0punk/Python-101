import smtplib

gmail_user = 'TU_CORREO'
gmail_password = 'TU CONTRASEÑA'

sent_from = gmail_user
to = ['CORREOS O CORREO DE DESTINO']
subject = 'PRUEBA CORREO ELECTRONICO'
body = 'ESTE ES UN TEXTO DE PRUEBA'

email_text = f"""\
From: {sent_from}
To: {", ".join(to)}
Subject: {subject}

{body}
"""

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
    print("Correo enviado exitosamente")
except smtplib.SMTPAuthenticationError:
    print("Error de autenticación: revise su usuario y contraseña")
except Exception as ex:
    print("Error al enviar correo:", ex)
