import requests
import smtplib
from email.message import EmailMessage

import os

API_KEY = os.environ["API_KEY"]

# City to monitor
CITY = "Kollam"

# Fetch weather data
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

# Get temperature
temp = data["main"]["temp"]

print(f"Temperature: {temp}°C")

# Check temperature condition
if temp > 35: 
    print("HOT WEATHER ALERT!")

    # Create email
    msg = EmailMessage()

    msg["Subject"] = "Weather Alert"
    msg["From"] = "weaselyronald79@gmail.com"
    msg["To"] = "teddylawsoncrew@gmail.com"

    msg.set_content(
        f"""
Weather Alert!

Current temperature in {CITY}: {temp}°C

Stay hydrated and take care.
"""
    )

    # Connect to Gmail SMTP
    server = smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    )

    EMAIL = os.environ["EMAIL"]
APP_PASSWORD = os.environ["APP_PASSWORD"]

server.login(
    EMAIL,
    APP_PASSWORD
)

    server.send_message(msg)

    server.quit()

    print("Email sent!")

else:
    print("Temperature is normal.")