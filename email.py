import smtplib, ssl

smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
  server.login(sender_email, password)
  server.sendmail(sender_email, receiver_email, message)
