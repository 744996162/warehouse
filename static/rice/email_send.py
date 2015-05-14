__author__ = 'Administrator'
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication



class EMail(object):
    def __init__(self,mail_addreass,mail_password,mail_user="",mail_host="",mail_postfix=""):
        self.mail_addreass=mail_addreass
        self.mail_password=mail_password
        self.mail_user=self.__get_user(self.mail_addreass,mail_user)
        self.mail_host=self.__get_host(self.mail_addreass,mail_host)
        self.mail_postfix=self.__get_postfix(self.mail_addreass,mail_postfix)

    @staticmethod
    def __get_user(mail_addreass,mail_user):
        if mail_user=="":
            stringArr=mail_addreass.strip().split("@")
            mail_user_temp=stringArr[0]
            return mail_user_temp
        else:
            return mail_user

    @staticmethod
    def __get_host(mail_password,mail_host):
        if mail_host=="":
            stringArr=mail_password.strip().split("@")
            mail_host_temp="smtp"+"."+stringArr[1]
            return mail_host_temp
        else:
            return mail_host

    @staticmethod
    def __get_postfix(mail_addreass,mail_postfix):
        if mail_postfix=="":
            stringArr=mail_addreass.strip().split("@")
            mail_postfix_temp=stringArr[1]
            return mail_postfix_temp
        else:
            return mail_postfix

    def send_mail(self,to_list,sub="hello",content="this is content"):
        mail_host=self.mail_host
        mail_user=self.mail_user
        mail_pass=self.mail_password
        mail_postfix=self.mail_postfix
        me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
        msg = MIMEMultipart(content)
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = to_list
        try:
            s = smtplib.SMTP()
            s.connect(mail_host)
            s.login(mail_user,mail_pass)
            s.sendmail(me, to_list, msg.as_string())
            s.close()
            return True
        except Exception as e:
            print(e)
            return False

if __name__=="__main__":
    test=EMail("744996162@qq.com","a1b2c3e48517343")
    to_list="744996162@qq.com"
    test.send_mail(to_list)
    print(test.mail_host,test.mail_user,test.mail_password,test.mail_postfix)
    # print(smt)