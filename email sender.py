from email.message import EmailMessage
import smtplib
import ssl
import getpass
msg = EmailMessage()
msg['Subject'] = 'Python Email Test'
msg['From'] = '<EMAIL>'
msg['To'] = '<EMAIL>'
msg.set_content('Python Email Test')

context = ssl.create_default_context()

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.login('<EMAIL>', 'password')
    smtp.send_message(msg)

