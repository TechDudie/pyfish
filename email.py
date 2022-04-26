import smtplib
import ssl

credentials = [i.split("=")[1] for i in open("email.conf").read().split("\n")]
smtp_server = credentials[0]
sender_email = credentials[1]
password = credentials[2]
receiver_email = input("Victim's Email Address: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
  server.login(sender_email, password)
  server.sendmail(sender_email, receiver_email, message)
