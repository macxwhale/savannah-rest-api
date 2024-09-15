import africastalking
import environ
import os
from pathlib import Path

# Setup environment and load variables
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Initialize Africa's Talking API
africastalking.initialize(username=env("AT_USERNAME"), api_key=env("AT_API_KEY"))
sms = africastalking.SMS

def send_sms(phone_number, message):

    recipients = [phone_number]   
    sender = env("AT_SENDER_ID")
    

    try:
        response = sms.send(message, recipients, sender)
        return response
    except Exception as e:
        return {'error': str(e)}
