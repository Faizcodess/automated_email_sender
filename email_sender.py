from email.message import EmailMessage #for email elements
import ssl  #for security while tranfering mails 
import smtplib  #to send emails we use simple mail transfer protocol library(inbuilt in python)
email_sender=""   #provide sender mail id
email_password=""   #generate an app password in google on your device
email_receiver=""   #provide receiver mail id
subject="This is my first automated mail using smtp"
body="Lets have fun with Python 😉"
em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smt:
    smt.login(email_sender,email_password)
    smt.sendmail(email_sender,email_receiver, em.as_string())