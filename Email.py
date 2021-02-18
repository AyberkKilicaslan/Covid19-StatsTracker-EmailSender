# YouTube Video: https://www.youtube.com/watch?v=mP_Ln-Z9-XY
import smtplib
USER_EMAIL = ""
MESSAGE = ""
SUBJECT = ""


def send_email(SUBJECT, MESSAGE):
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login('sender email', 'password')
    message = 'Subject: {}\n\n{}'.format(SUBJECT, MESSAGE)
    print(message)
    server.sendmail('sender email', USER_EMAIL, message)
    server.quit()
    print("Success: Email sent!")


