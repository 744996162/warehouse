#ecoding=utf-8
__author__ = 'Administrator'
import pymongo
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from conf import *
base_path = "/home/huolibi/data/"
file_in_path2 = "G:/data/new_fileau"
error_path = base_path + "error.data"

#file_in_linux_path = "/home/huolibi/data/user_order_test"
file_in_linux_path = base_path + "new_fileaa"




file_in = open(file_in_linux_path)
errpr_file = open(error_path, "a")

con_local=pymongo.Connection(host="localhost", port=27017)
db = con_local.admin
db.authenticate("gtgj","gtgj")
db = con_local.gtgj
dict_list = []

file_lines = len(file_in.readlines())
# print(file_lines)
file_in = open(file_in_linux_path)
# uid,p_info,account,order_date,i_status,depart_date,depart_name,arrive_name,ticket_count,train_no,amount,create_time
for (count, line) in enumerate(file_in):
    # print(count)
    stringArr = line.strip().split("\t")
    # dict_list = []
    # print(count)
    try:
        uid = stringArr[0]
        p_info = stringArr[1]
        account = stringArr[2]
        order_date = stringArr[3]
        s_order_date = order_date[0:4]+order_date[5:7]+order_date[8:10]
        i_order_date = int(s_order_date)
        i_status = stringArr[4]
        depart_date = stringArr[5]
        i_depart_date = int(depart_date[0:4]+depart_date[5:7]+depart_date[8:10])

        depart_name = stringArr[6]
        arrive_name = stringArr[7]
        depart_code, depart_city_code = getCode(depart_name.encode('gbk'))
        arrive_code, arrive_city_code = getCode(arrive_name.encode('gbk'))

        ticket_count = int(stringArr[8])
        train_no = stringArr[9]
        amount = float(stringArr[10])
        create_time = datetime.datetime.strptime(stringArr[11], "%Y-%m-%d %H:%M:%S")
        t = {"uid": uid, "p_info": p_info, "account": account, "order_date": i_order_date,
         "i_status": i_status, "depart_date": i_depart_date, "depart_name": depart_name, "depart_code":depart_code, "depart_city_code":depart_city_code,
         "arrive_name": arrive_name, "arrive_code":arrive_code, "arrive_city_code":arrive_city_code,
         "ticket_count": ticket_count, "train_no": train_no, "amount": amount, "create_time": create_time}
        dict_list.append(t)
        # conf.order.insert(t)
    except Exception as e:
        errpr_file.write(line)
        # print(Exception)
        # print(line)
    if count % 10000 == 0 or (count == (file_lines-1)):
        # print dict_list
        print(db.order.insert(dict_list))
        dict_list = []

    # print(uid,p_info,account, order_date)
