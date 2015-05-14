#ecoding=utf-8
__author__ = 'Administrator'
import os
import xlwt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime
from email.mime.image import MIMEImage

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
def getYestaday():
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(days=-1)
    return yes_time.strftime('%Y%m%d')

def excel_write(text_in="0128/result.txt",excel_out="0128/result0128.xls",table_name="sheet1"):
    fr_in=open(text_in)
    wbk=xlwt.Workbook(encoding='utf-8')
    sheet=wbk.add_sheet(table_name,True)
    for i,line in enumerate(fr_in.readlines()):
        stringArr=line.strip().split("\t")
        for j,str in enumerate(stringArr):
            if j==6:
                str=int(str)
            sheet.write(i,j,str)
        # print i,stringArr
    export=excel_out
    wbk.save(export)
    return excel_out


def excel_write2(text_in1="0128/result.txt",text_in2="0128/error.txt",excel_out="0128/result0128.xls",table_name1="sheet1",table_name2="sheet2"):
    fr_in1=open(text_in1)
    fr_in2=open(text_in2)
    wbk=xlwt.Workbook(encoding='utf-8')
    sheet1=wbk.add_sheet(table_name1,True)
    for i,line in enumerate(fr_in1.readlines()):
        stringArr=line.strip().split("\t")
        for j,str in enumerate(stringArr):
            if j==6:
                str=int(str)
            sheet1.write(i,j,str)

    sheet2=wbk.add_sheet(table_name2,True)
    for i,line in enumerate(fr_in2.readlines()):
        stringArr=line.strip().split("\t")
        for j,str in enumerate(stringArr):
            if j==6:
                str=int(str)
            sheet2.write(i,j,str)

    export=excel_out
    wbk.save(export)
    return excel_out


def send_mail(to_list,sub,content):
    #############
    #to_list为收件人
    #sub为邮件标题
    #content为邮件内容
    ###############
    #设置服务器，用户名、口令以及邮箱的后缀
    mail_host="smtp.qq.com"
    mail_user="744996162"
    mail_pass="a1b2c3e48517343"
    mail_postfix="qq.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
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


def send_mail2(to_list,sub,content,attach_file="0128/result.txt"):
    #############
    #to_list为收件人
    #sub为邮件标题
    #content为邮件内容
    ###############
    #设置服务器，用户名、口令以及邮箱的后缀
    mail_host="smtp.qq.com"
    mail_user="744996162"
    mail_pass="a1b2c3e48517343"
    mail_postfix="qq.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg=MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list


    att = MIMEApplication(file(attach_file, 'rb').read())
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('content-disposition','attachment',filename=attach_file)
    msg.attach(att)
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

    pass

def send_mail_attach_dir(to_list,sub,content,dir_path="20150128"):
    #############
    #to_list为收件人
    #sub为邮件标题
    #content为邮件内容
    ###############
    #设置服务器，用户名、口令以及邮箱的后缀
    mail_host="smtp.qq.com"
    mail_user="744996162"
    mail_pass="a1b2c3e48517343"
    mail_postfix="qq.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg=MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list


    path_list=get_all_file(dir_path)
    for file_path in path_list:
        try:
            att = MIMEApplication(file(file_path, 'rb').read())
            att["Content-Type"] = 'application/octet-stream'
            att.add_header('content-disposition','attachment',filename=file_path)
            msg.attach(att)
        except Exception as e:
            print(e)

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
    pass



def get_all_file(dir_path="20150128"):
    file_list = []
    if dir_path is None:
        raise Exception("floder_path is None")
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for name in filenames:
            # print(name)
            file_list.append(dirpath + '/' + name)
    return file_list



if __name__=="__main__":
    # excel_write2()
    # to_list="744996162@qq.com"
    # send_mail2(to_list,"hello","mail test")

    floder_path="20150128"
    file_list=get_all_file(floder_path)
    for i in file_list:
        print i
    pass
    to_list="744996162@qq.com"
    send_mail_attach_dir(to_list,"hello","mail test")