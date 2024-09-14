import smtplib
import ssl
context = ssl.create_default_context()
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "varshithat.ug22.cs@francisxavier.ac.in"  # Enter your address
receiver_email = "varshi141178@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)