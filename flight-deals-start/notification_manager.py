
import smtplib
from email.mime.text import MIMEText

class NotificationManager:

    def __init__(self, sender, password) -> None:
        self._sender = sender
        self._password = password 

    def send_email(self, subject, body, recipients):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self._sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self._sender, self._password)
            smtp_server.sendmail(self._sender, recipients, msg.as_string())
        print("Message sent!")