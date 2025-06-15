import smtplib
from email.mime.text import MIMEText
from chatbot.chatbot_logic import *

def send_leave_email(data):
    sender = "your_email@gmail.com"
    password = "your_app_password"
    receiver = "manager@example.com"

    msg = MIMEText(generate_leave_letter(data))
    msg['Subject'] = "Leave Application"
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
