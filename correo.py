


#DESACTIVAR VERIFICACION EN DOS PASOS DE GOOGLE Y ACTIVAR EL ENVIO DE EMAILS DE APLICACIONES NO SEGURAS



import smtplib




gmail_user = 'TU_CORREO'
gmail_password = 'TU CONTRASEÑA'

sent_from = gmail_user
to = ['CORREOS O CORREO DE DESTINO']
subject = 'PRUEBA CORREO ELECTRONICO'
body = 'ESTE ES UN TEXTO DE PRUEBA'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)