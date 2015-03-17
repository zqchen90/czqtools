import smtplib
import sys
from email.mime.text import MIMEText

class Mail:
    """docstring for Mail"""
    def __init__(self, host, port, username, password, email):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.email = email
        self.loginFlag = False;
        self.smtp = smtplib.SMTP()

    def __del__(self):
        # disconnect from host
        self.quit()

    def login(self):
        try:
            self.smtp.connect(self.host, self.port)
            self.smtp.login(self.username, self.password)
            self.loginFlag = True
        except:
            self.printMsg("Error: fail to login")
            self.loginFlag = False

    def quit(self):
        try:
            self.smtp.quit()
        except:
            self.printMsg("Error: fail to quit")

    def sendTextMail(self, senderName, toAddressList, subject, content):
        if self.loginFlag == False:
            self.login()
        if self.loginFlag == False:
            self.printMsg("Error: can't send mail now")
            return False

        me = senderName +"<"+self.email+">"
        msg = MIMEText(content,_charset='gbk') 
        msg['Subject'] = subject
        msg['From'] = me 
        msg['To'] = ";".join(toAddressList) 
        try:
            self.smtp.sendmail(me, toAddressList, msg.as_string())
            self.printMsg("Successfully sent email")
            return True
        except:
            self.printMsg("Error: unable to send email")
        return False

    def printMsg(self, msg):
        print msg, sys.exc_info()[0]
