import  os
import smtplib
from email.mime.multipart import MIMEMultipart

from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication

#账号信息
to_addr=[xxxxxxxx]
from_addr=xxxxxxxxxx
subject ="接口测试报告"
content="已发邮件注意查收"
smtpserver = 'xxxxxx'
username = 'xxxxx'
password='xxxx'

def getfile(filename):
    (filepath,filename) = os.path.split(filename)


def emailmodel(adr):
    (filepath,filename) = os.path.split(adr)
    msg = MIMEMultipart()
    # 邮件内容读取
    mime = MIMEApplication(open(adr,"rb").read())
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=filename)
    #添加到邮件模板
    msg.attach(mime)
    msg.attach(MIMEText('%s'%content))
    msg['From'] = from_addr
    msg['To'] =','.join(to_addr)
    msg['Subject'] = Header('%s'%subject, 'utf-8')
    return  msg

def duqu(adr):
    smtp = smtplib.SMTP(smtpserver) # SMTP协议默认端口是25
    smtp.login(username, password)
    smtp.sendmail(from_addr,to_addr, emailmodel(adr).as_string())
    smtp.quit()


if __name__=="__main__":
    adr="d://post.xls"
    getfile("d://post.xls")





