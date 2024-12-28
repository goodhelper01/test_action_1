import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender="goodhelper01@gmail.com"
receiver=["newdragon21@gmail.com","newdragon29@gmail.com"]
appmima="npgq vzgy mssy wbhh"

for i in receiver:    
    msg=MIMEMultipart()
    msg["From"]=sender
    msg["To"]=i
    msg["Subjet"]=Header("Test send email","utf-8").encode()
    
    #body="This is send by python\n"
    #body2="how are you?"

    msg_text=MIMEText("This is send by python")
    msg.attach(msg_text)
    c=ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c)as server:
        server.login(sender,appmima)
        server.sendmail(sender,i,msg.as_string())
    print("success send mail")
