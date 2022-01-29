import smtplib, ssl
from libs.applibs.speak import speak

def sendEmail(receiver):
    '''
    Send an email
    '''
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "trang.testjavis@gmail.com"  # Enter your address
    #password = input("Type your password and press enter: ")
    password = "javis.1602"
    
    # Get receiver address
    dict_email = {"apple":"linhtrang1602.hust@gmail.com","jenny":"trang.testjavis+01@gmail.com",
                  "me":"trang.testjavis+01@gmail.com"}
    receiver_email = dict_email[receiver]  
    #print(receiver_email)
    
    # message
    message1 = """\
From: Trang Nguyen Linh <trang.testjavis@gmail.com>
Subject: Re: I am out of the office
Greetings,

Thank you for your email. I am out of the office and will be back soon. During this period I will have limited access to my email. 

For immediate assistance please contact me on my cell phone at 0123.456.789

Best regards,

Trang Nguyen Linh"""
   
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message1)
    speak("Email sending is completed!")

#sendEmail("apple")