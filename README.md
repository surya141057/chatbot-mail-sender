📧 Chatbot Mail Sender
This project is a Django-based chatbot that interacts with users to collect leave request details and sends a professional leave letter via email using OpenAI's GPT model.

🧠 Features
Collects leave details from the user via chat.

Generates a professional leave letter using OpenAI API.

Sends the generated letter via email to the recipient.

Web API endpoint for chatbot interaction (/chatbot/).

🗂️ Project Structure
chatbot-mail-sender/
│
├── chatbotenv/                # Virtual environment (not pushed to Git)
├── mailbot/                   # Main Django project
│   ├── chatbot/               # Django app for chatbot
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── views.py           # Contains chatbot_view function
│   │   ├── chatbot_logic.py   # Chat logic + OpenAI integration
│   │   └── email_sender.py    # Email sending logic
│   ├── wsgi.py
│   └── urls.py                # URL routing
│
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django command-line utility
├── .env                       # Stores environment variables (API keys, passwords)
🔧 Setup Instructions

1. Clone the Repository
git clone https://github.com/your-username/chatbot-mail-sender.git
cd chatbot-mail-sender

3. Set up Virtual Environment
python -m venv chatbotenv
source chatbotenv/bin/activate  # Linux/macOS
chatbotenv\Scripts\activate     # Windows

4. Install Dependencies
pip install -r requirements.txt
If requirements.txt is not created, you can install manually:
pip install django openai python-dotenv

5. Configure Environment Variables
Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
6. Apply Migrations and Run Server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

7. Use the Chatbot
Send a POST request to the endpoint:

http
POST http://localhost:8000/chatbot/
Content-Type: application/json

{
  "message": "I want to take a leave"
}
The chatbot will walk you through the steps to gather details and generate/send the leave letter.

📧 Sending Emails
Make sure you enable "App Passwords" in Gmail if you're using Gmail.

Set the EMAIL_USER and EMAIL_PASSWORD in .env properly.

💬 Example Conversation Flow
User: "I want to take a leave"

Bot: "Got it. What's the email address of your receiver?"

User: "manager@example.com"

Bot: "What's the sender name?"

... (goes through reason, dates)

Bot: Generates leave letter

User: "Send"

Bot: "Your leave letter has been sent successfully!"
