
import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

username = os.getenv("FOODNUTRI_SMTP_USERNAME")
password = os.getenv("FOODNUTRI_SMTP_PASSWORD")

msg = EmailMessage()
msg["Subject"] = "FoodNutri SMTP Test"
msg["From"] = username
msg["To"] = username
msg.set_content("FoodNutri email sending test successful!")

try:
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.send_message(msg)

    print("SUCCESS: Test email sent!")

except Exception as e:
    print("FAILED:", repr(e))
