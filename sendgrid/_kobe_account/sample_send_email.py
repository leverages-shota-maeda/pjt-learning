# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), 'sendgrid.env')
load_dotenv(dotenv_path)
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


if __name__ == '__main__':
  message = Mail(
      from_email='s.maeda.kobe@gmail.com',
      to_emails='s.maeda.kobe@gmail.com',
      subject='Sending with Twilio SendGrid is Fun',
      html_content='<strong>and easy to do anywhere, even with Python</strong>')
  try:
      sg = SendGridAPIClient(SENDGRID_API_KEY)
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
  except Exception as e:
      print(e.message)