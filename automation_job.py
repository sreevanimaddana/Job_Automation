import yagmail
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

def send_email():
    today = datetime.now().strftime("%Y-%m-%d")

    body = f"""
Daily Entry-Level Data Analyst Jobs — {today}

Indeed:
https://www.indeed.com/jobs?q=entry+level+data+analyst

LinkedIn:
https://www.linkedin.com/jobs/search/?keywords=entry%20level%20data%20analyst

(Remember to log in to LinkedIn to see full results)
"""

    yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)
    yag.send(
        to=EMAIL_RECEIVER,
        subject="Daily Data Analyst Job Links",
        contents=body
    )
    print("Email sent successfully!")

if __name__ == "__main__":
    send_email()

