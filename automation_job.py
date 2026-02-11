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
https://www.indeed.com/jobs?q="data+analyst"+("entry+level"+OR+"fresher"+OR+"junior")+-senior+-manager+-lead

LinkedIn:
https://www.linkedin.com/jobs/search/?keywords=Data%20Analyst%20(entry%20level%20OR%20fresher%20OR%20junior)%20-NOT%20senior%20-NOT%20manager


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

