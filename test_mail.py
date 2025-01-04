import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders

sender="寄信者@gmail.com"
receiver=["收信者1@gmail.com","收信者2@gmail.com"]
appmima="idci zwub rtqj msev"  #google應用程式密鑰

for i in receiver:    
    msg=MIMEMultipart()
    msg["From"]=sender
    msg["To"]=i
    msg["Subjet"]=Header("Test send email","utf-8").encode() #編碼記得改utf-8不然可能會亂碼
    
    body="This is send by python\n"
    body2="how are you?"

    msg_text=MIMEText(body+body2)
    msg.attach(msg_text)

    text_path = "new/test.txt"    #目前用相對路徑

    with open(text_path,"r") as f: #將f: = text_path 用 as 放入 open()中
        part = MIMEBase("application","octet-stream")  #設定格式相關
        part.set_payload(f.read()) #同上讀 f
        encoders.encode_base64(part) #記得編碼
        part.add_header('Content-Disposition','attachment; filename="'+text_path+'"') #filename掛接可以另取名字
        msg.attach(part)
    
    c=ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c)as server: #smtp.gmail.com 預設port是 465
        server.login(sender,appmima)
        server.sendmail(sender,i,msg.as_string())
    print("success send mail") #列印確認寄信成功
