#ecoding=utf-8
__author__ = 'Administrator'
import source_gift_order
import text_cal
from tools import excel_write2
from tools import getYestaday
from tools import send_mail_attach_dir
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



def main():
    #查询数据
    yestoday=getYestaday()
    sql="SELECT orderid,phoneid,extdata,createtime " \
        "FROM gift_order " \
        "WHERE TYPE = 16 " \
        "and DATE_FORMAT(createtime,'%%Y%%m%%d')=%s "  % yestoday
    file_path=yestoday
    results_path=file_path+"/"+"gift_order.txt"
    result_temp=file_path+"/"+"temp.txt"
    result1_path=file_path+"/"+"result.txt"
    result2_path=file_path+"/"+"error.txt"
    excel_path=file_path+"/"+"0128.xls"

    query_obj=source_gift_order.QueryResultDao_nfields()
    results=query_obj.get_users(sql)
    results_path=query_obj.query_result_to_txt(results,'0128/gift_order.txt')
    result_temp=text_cal.text_rice(results_path,'0128/temp.txt')
    #遍历，及解析输出
    result1,result2=text_cal.text_string_jieba3(result_temp,"0128/result.txt","0128/error.txt")
    excel_path=excel_write2(result1,result2,"0128/0128.xls")

    # to_list="744996162@qq.com"
    # send_mail_attach_dir(to_list,yestoday+"数据",yestoday+"数据",yestoday)

def main2():
    #查询数据
    # os.mkdir("file")
    yestoday=getYestaday()
    if os.path.exists(yestoday):
        pass
    else:
        os.mkdir(yestoday)

    sql="SELECT orderid,phoneid,extdata,createtime " \
        "FROM gift_order " \
        "WHERE TYPE = 16 " \
        "and p not like '%%,hbgj,%%' " \
        "and DATE_FORMAT(createtime,'%%Y%%m%%d')=%s "  % yestoday
    file_path=yestoday
    results_path=file_path+"/"+"gift_order.txt"
    result_temp_path=file_path+"/"+"temp.txt"
    result1_path=file_path+"/"+"result.txt"
    result2_path=file_path+"/"+"error.txt"
    excel_path=file_path+"/"+yestoday+".xls"

    query_obj=source_gift_order.QueryResultDao_nfields()
    results=query_obj.get_users(sql)

    results_path=query_obj.query_result_to_txt(results,results_path)

    result_temp=text_cal.text_rice(results_path,result_temp_path)

    #遍历，及解析输出
    result1,result2=text_cal.text_string_jieba3(result_temp,result1_path,result2_path)
    excel_path=excel_write2(result1,result2,excel_path)
    # to_list="744996162@qq.com"
    # send_mail_attach_dir(to_list,yestoday+"rice data",yestoday+"rice data",yestoday)


def main_hb():
    #查询数据
    # os.mkdir("file")
    yestoday=getYestaday()
    if os.path.exists(yestoday):
        pass
    else:
        os.mkdir(yestoday)

    sql_hb="SELECT orderid,phoneid,extdata,createtime " \
        "FROM gift_order " \
        "WHERE TYPE = 16 " \
        "and p  like '%%,hbgj,%%' " \
        "and DATE_FORMAT(createtime,'%%Y%%m%%d')=%s "  % yestoday
    file_path=yestoday
    results_path=file_path+"/"+"gift_order_hb.txt"
    result_temp_path=file_path+"/"+"temp_hb.txt"
    result1_path=file_path+"/"+"result_hb.txt"
    result2_path=file_path+"/"+"error_hb.txt"
    excel_path=file_path+"/"+yestoday+"hb.xls"

    query_obj=source_gift_order.QueryResultDao_nfields()
    results=query_obj.get_users(sql_hb)

    results_path=query_obj.query_result_to_txt(results,results_path)

    result_temp=text_cal.text_rice(results_path,result_temp_path)

    #遍历，及解析输出
    result1,result2=text_cal.text_string_jieba3(result_temp,result1_path,result2_path)
    excel_path=excel_write2(result1,result2,excel_path)

def main_gt():
    #查询数据
    # os.mkdir("file")
    yestoday=getYestaday()
    if os.path.exists(yestoday):
        pass
    else:
        os.mkdir(yestoday)

    sql_gt="SELECT orderid,phoneid,extdata,createtime " \
        "FROM gift_order " \
        "WHERE TYPE = 16 " \
        "and p not like '%%,hbgj,%%' " \
        "and DATE_FORMAT(createtime,'%%Y%%m%%d')=%s "  % yestoday
    file_path=yestoday
    results_path=file_path+"/"+"gift_order_gt.txt"
    result_temp_path=file_path+"/"+"temp_gt.txt"
    result1_path=file_path+"/"+"result_gt.txt"
    result2_path=file_path+"/"+"error_gt.txt"
    excel_path=file_path+"/"+yestoday+"gt.xls"

    query_obj=source_gift_order.QueryResultDao_nfields()
    results=query_obj.get_users(sql_gt)

    results_path=query_obj.query_result_to_txt(results,results_path)

    result_temp=text_cal.text_rice(results_path,result_temp_path)

    #遍历，及解析输出
    result1,result2=text_cal.text_string_jieba3(result_temp,result1_path,result2_path)
    excel_path=excel_write2(result1,result2,excel_path)

def main_query_date(query_date=""):
    #查询数据
    # os.mkdir("file")
    if query_date=="":
        query_date=getYestaday()
    else:
        pass
    if os.path.exists(query_date):
        pass
    else:
        os.mkdir(query_date)

    sql="SELECT orderid,phoneid,extdata,createtime " \
        "FROM gift_order " \
        "WHERE TYPE = 16 " \
        "and DATE_FORMAT(createtime,'%%Y%%m%%d')=%s "  % query_date
    file_path=query_date
    results_path=file_path+"/"+"gift_order.txt"
    result_temp_path=file_path+"/"+"temp.txt"
    result1_path=file_path+"/"+"result.txt"
    result2_path=file_path+"/"+"error.txt"
    excel_path=file_path+"/"+query_date+".xls"

    query_obj=source_gift_order.QueryResultDao_nfields()
    results=query_obj.get_users(sql)

    results_path=query_obj.query_result_to_txt(results,results_path)

    result_temp=text_cal.text_rice(results_path,result_temp_path)

    #遍历，及解析输出
    result1,result2=text_cal.text_string_jieba3(result_temp,result1_path,result2_path)
    excel_path=excel_write2(result1,result2,excel_path)
    # to_list="744996162@qq.com"
    # send_mail_attach_dir(to_list,yestoday+"rice data",yestoday+"rice data",yestoday)

def mainSendEmail():
    try:
        main_hb()
        main_gt()
    except Exception as e:
        print e
    yestoday=getYestaday()
    to_list="744996162@qq.com"
    send_mail_attach_dir(to_list,yestoday+"rice data",yestoday+"rice data",yestoday)

if __name__=="__main__":
    # print(BASE_DIR )
    # main()
    # print(getYestaday(),type(getYestaday()))
    # query_date="20150130"
    # main_query_date(query_date)

    # main2()

    # main_gt()
    # main_hb()

    # mainSendEmail()



    # main_gt()
    # main_hb()
    query_date="20150213"
    main_query_date(query_date)

    pass