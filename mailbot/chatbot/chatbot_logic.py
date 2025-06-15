import os
from openai import OpenAI
from chatbot.email_sender import send_leave_email 
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

chat_context = {}
def generate_leave_letter(data):
    prompt = (
        f"Write a professional leave letter for the following:\n"
        f"Reason: {data['reason']}\n"
        f"Start Date: {data['start_date']}\n"
        f"End Date: {data['end_date']}\n"
        f"Sender Name: {data.get('sender_name', '[Your Name]')}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

def process_chat(user_input):
    global chat_context

    # if "leave" in user_input.lower() and not chat_context:
    #     chat_context["stage"] = "reason"
    #     return "Sure, what's the reason for your leave?"
    
    if "leave" in user_input.lower() and not chat_context:
        chat_context["stage"] = "receiver_mail"
        return "Got it. What's the email address of your receiver?"
    
    # if chat_context.get("stage") == "sender_mail":
    #     chat_context["sender_mail"] = user_input
    #     chat_context["stage"] = "receiver_mail"
    #     return "Got it. What's the email address of your receiver?"
    
    # if chat_contex    t.get("stage") == "sender_password":
    #     chat_context["sender_password"] = user_input
    #     chat_context["stage"] = "receiver_mail"
    #     return "Got it. What's the email address of your manager?"

    if chat_context.get("stage") == "receiver_mail":
        chat_context["receiver_mail"] = user_input
        chat_context["stage"] = "sender_name"
        return "Got it. What's the sender name?"
    
    if chat_context.get("stage") == "sender_name":
        chat_context["sender_name"] = user_input
        chat_context["stage"] = "reason"
        return "Got it. What's the reason for your leave?"

    if chat_context.get("stage") == "reason":
        chat_context["reason"] = user_input
        chat_context["stage"] = "start_date"
        return "Got it. What's the start date of your leave?"

    if chat_context.get("stage") == "start_date":
        chat_context["start_date"] = user_input
        chat_context["stage"] = "end_date"
        return "And the end date?"

    if chat_context.get("stage") == "end_date":
        chat_context["end_date"] = user_input
        chat_context["stage"] = "confirm"
        return generate_leave_letter(chat_context)

    if "send" in user_input.lower() and chat_context:
        send_leave_email(chat_context)
        chat_context = {}  # reset
        return "Your leave letter has been sent successfully!"

    return "I'm here to help you generate and send a leave letter."
def send_leave_email(data):
    password = os.getenv("EMAIL_PASSWORD")
    sender = os.getenv("EMAIL_USER")
    receiver = chat_context["receiver_mail"] 

    msg = MIMEText(generate_leave_letter(data))
    msg['Subject'] = "Leave Application"
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())