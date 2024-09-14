import smtplib
import ssl
smtp_server ="smtp.gmail.com"
port=465 #for ssl
context=ssl.create_default_context()
sender_email="varshithat.ug22.cs@francisxavier.ac.in"#Enter your address
receiver_email="varshi141178@gmail.com"#enter receiver address
password=input("type password and press enter:")
message="""\
Subject:Hi there,how are u varshu?

This message is sent from python"""

with smtplib.SMTP_SSL(port, smtp_server, context=context) as server:
     server.login(sender_email,password)
     server.sendmail(sender_email,receiver_email,message)