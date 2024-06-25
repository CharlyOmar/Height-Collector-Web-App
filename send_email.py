from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email="example@domain.com"
    from_password = "thisIsThePassword01"
    to_email = email

    subject="Height data"
    message = "Hello there. Your height is <strong>. Average height of all is %s and that is caculated out %s of people.</strong>" % (height, average_height, count)
    

    msg = MIMEText(message, "html")
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)