import smtplib
from email.message import EmailMessage

def sendmail(name, receiver):
    email = "Put sender email"
    msg = EmailMessage()
    msg['Subject'] = "put email title"
    msg['From'] = email
    msg['To'] = [] #put receiver emails

    msg.set_content(f"Hi {name}:\n...")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email, "put app password here")
        print("Login Success")
        smtp.send_message(msg)
        print("Mail sent to", receiver)


sendmail("put names", "put emails")
