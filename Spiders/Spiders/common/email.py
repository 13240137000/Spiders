import smtplib
from email.mime.text import MIMEText
import logging


class EmailHelper(object):

    def __init__(self):

        self.logging = logging.getLogger('Warning')
        self.email_host = ''
        self.email_port = ''
        self.email_account = ''
        self.email_password = ''
        self.email_email_address = ""

    def send_text_email(self, address, subject, content):

        message_text = MIMEText(content, 'plain', 'utf8')
        message_text['From'] = self.email_email_address
        message_text['To'] = address
        message_text['Subject'] = subject

        try:

            client = smtplib.SMTP(host=self.email_host, port=self.email_port)
            login_result = client.login(self.email_account, self.email_password)

            print(login_result)

            if login_result and login_result[0] == 235:
                client.sendmail(self.email_email_address, address, message_text.as_string())
            else:
                self.logging.error('Sorry, we are got error from send email：login result is {} - {}'.format(login_result[0], login_result[1]))

        except Exception as e:

            self.logging.error('Sorry we are got error from login to email server：{}'.format(e))
