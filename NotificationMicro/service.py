import os

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'artemchege@gmail.com')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '1234')
MAIL_FROM = os.environ.get('MAIL_FROM', 'artemchege@gmail.com')
MAIL_PORT = 587
MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
MAIL_FROM_NAME = os.environ.get('MAIL_FROM_NAME', 'Fast api microservice')


conf = ConnectionConfig(
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_FROM=MAIL_FROM,
    MAIL_PORT=MAIL_PORT,
    MAIL_SERVER=MAIL_SERVER,
    MAIL_FROM_NAME=MAIL_FROM_NAME,
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)


async def send_email_async(subject: str, email_to: str, body: str) -> None:
    """ Send email asynchronously """

    message = MessageSchema(subject=subject, recipients=[email_to], body=body)
    fm = FastMail(conf)
    await fm.send_message(message, template_name='email.html')
