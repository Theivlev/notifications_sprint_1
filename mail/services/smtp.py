import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from core.config import smtp_settings
from services.template import get_template


async def send_email_smtp(email, subject, template, data):
    server = smtplib.SMTP(smtp_settings.host, smtp_settings.port)
    server.starttls()  # Включаем шифрование
    server.login(smtp_settings.user, smtp_settings.password)

    body = get_template(template, data)

    msg = MIMEMultipart()
    msg["From"] = smtp_settings.user
    msg["To"] = email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    server.send_message(msg)
