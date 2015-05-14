#ecoding=utf-8
__author__ = 'Administrator'
import pymongo
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from stationCode import *
from file_search import *
base_path = "/home/huolibi/data/"


def get_db(dbtype="local"):
    if dbtype == "169server":
        con_local = pymongo.Connection(host="localhost", port=27017)
        db = con_local.admin
        db.authenticate("gtgj", "gtgj")
        db = con_local.gtgj
    else:
        con_local = pymongo.Connection(host="localhost", port=27017)
        db = con_local.gtgj
    return db

def get_file_list(file_name_list, error_file_name):

    file_in_path_list = []
    for file_name in file_name_list:
        file_in_path_list.append(base_path+file_name)
    error_path = base_path + error_file_name
    return file_in_path_list, error_path




def data_in(file_in_path, error_path, dbtype):
    file_in = open(file_in_path)
    error_file = open(error_path, "a")
    file_lines = len(file_in.readlines())
    file_in = open(file_in_path)

    db = get_db(dbtype)
    dict_list = []
    for (count, line) in enumerate(file_in):
        stringArr = line.strip().split("\t")
        # print line

        try:
            t = {}

            uid = stringArr[0]
            t["uid"] = uid

            p_info = stringArr[1]
            t["p_info"] = p_info

            if "ios" in p_info:
                platform = "ios"
            else:
                platform = "android"
            t["platform"] = platform

            account = stringArr[2]
            t["account"] = account

            i_status = stringArr[4]
            t["i_status"] = i_status

            depart_date = stringArr[5]
            try:
                i_depart_date = int(depart_date[0:4]+depart_date[5:7]+depart_date[8:10])
                t["depart_date"] = i_depart_date
            except Exception as e:
                pass

            depart_name = stringArr[6]
            arrive_name = stringArr[7]
            depart_code, depart_city_code = getCode(depart_name.encode('gbk'))
            arrive_code, arrive_city_code = getCode(arrive_name.encode('gbk'))

            t["depart_code"] = depart_code
            t["depart_city_code"] = depart_city_code
            t["arrive_code"] = arrive_code
            t["arrive_city_code"] = arrive_city_code

            ticket_count = int(stringArr[8])
            t["ticket_count"] = ticket_count

            train_no = stringArr[9]
            t["train_no"] = train_no

            amount = float(stringArr[10])
            t["amount"] = amount

            create_time = datetime.datetime.strptime(stringArr[11], "%Y-%m-%d %H:%M:%S")
            t["create_time"] = create_time
 
            try:
                t["order_date"] = int(create_time.strftime("%Y%m%d"))
            except Exception as e:
                pass
            if stringArr[12] == "\N":
                t["pay_method"] = "None"
            else:
                t["pay_method"] = stringArr[12]

            try:
                t["pay_time"] = datetime.datetime.strptime(stringArr[13], "%Y-%m-%d %H:%M:%S")
            except Exception as e:
                pass

           # t = {"uid": uid, "p_info": p_info, "account": account, "order_date": i_order_date, "platform": platform,
            #  "i_status": i_status, "depart_date": i_depart_date, "depart_name": depart_name, "depart_code": depart_code, "depart_city_code":depart_city_code,
            #  "arrive_name": arrive_name, "arrive_code": arrive_code, "arrive_city_code": arrive_city_code,
            #  "ticket_count": ticket_count, "train_no": train_no, "amount": amount, "create_time": create_time}

            dict_list.append(t)
            # print(dict_list)

        except Exception as e:
            # print(e)
            error_file.write(line)

        if count % 10000 == 9999 or (count == (file_lines-1)):
            # print dict_list
            print (file_in_path, str(count+1))
            db.order.insert(dict_list)
            dict_list = []

def insert_onefile():

    file_name_list =["user_order20150104.txt"]
    #file_name_list = ["user_order_test0416.txt"]
    error_file_name = "error_order_20150104.txt"
    file_list_path,err_path = get_file_list(file_name_list, error_file_name)
    for file_name in file_list_path:
        data_in(file_name, err_path, "169server")
        print file_name
    print len(file_list_path)

# def main2():
#     data_path = "G:/data/gt_order_all/wrong/user_order_history_20140825_20140420_20140423"
#     error_file_path = "G:/data/gt_order_all/wrong/error_test.log"
#     data_in(data_path, error_file_path, "local")
#     pass

def insert_folder():
    data_folder = "/home/huolibi/data/gt_order_all/order/"
    error_path = "/home/huolibi/data/error_order20140825end.log"
    code_error = open("/home/huolibi/data/code_error20140825.log", "a")

    # data_folder = "G:/data/gt_order_all/wrong/"
    # error_path = "G:/data/gt_order_all/error_test0415.log"
    # code_error = open("G:/data/gt_order_all/code_errortest0415.log", "a")
    data_path_list = sorted(get_all_file(data_folder))

    print(data_path_list)
    for file_path in data_path_list:
          # print(file_path)
        try:
            data_in(file_path, error_path, "169server")
        except Exception as e:
            # print(e)
            code_error.write(file_path+"\n")
            pass
    # print len(file_list_path)
    pass


if __name__ == "__main__":
    file_in_path = "G:/data/user_sub_order_test.txt"
    error_path = "G:/data/user_sub_error.log"
    # data_in(file_in_path, error_path, "")
    insert_folder()
    #insert_onefile()
    pass
