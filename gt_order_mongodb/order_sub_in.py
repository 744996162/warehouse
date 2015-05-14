#ecoding=utf-8
__author__ = 'Administrator'
import pymongo
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from stationCode import *
base_path = "/home/huolibi/data/"

def get_db(dbtype="local"):
    if dbtype == "169server":
        con_local=pymongo.Connection(host="localhost", port=27017)
        db = con_local.admin
        db.authenticate("gtgj", "gtgj")
        db = con_local.gtgj
    else:
        con_local=pymongo.Connection(host="localhost", port=27017)
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

        try:
            order_id = stringArr[0]
            uid = stringArr[1]
            account = stringArr[2]
            p_info = stringArr[3]
            if "ios" in p_info:
              platform = "ios"
            else :
              platform = "android"
            depart_date = stringArr[4]
            i_depart_date = depart_date[0:4]+depart_date[5:7]+depart_date[8:10]

            train_no = stringArr[5]

            depart_name = stringArr[6]
            arrive_name = stringArr[7]
            depart_code, depart_city_code = getCode(depart_name.encode('gbk'))
            arrive_code, arrive_city_code = getCode(arrive_name.encode('gbk'))

            name = stringArr[8]
            card_type = stringArr[9]
            card_no = stringArr[10]
            phone = stringArr[11]
            seat_name = stringArr[12]
            ticket_type = stringArr[13]
            status = stringArr[14]
            price = float(stringArr[15])
            create_time = datetime.datetime.strptime(stringArr[16], "%Y-%m-%d %H:%M:%S")


            t = {"order_id": order_id, "uid": uid, "account": account,"p_info": p_info, "depart_date": i_depart_date,
                 "train_no":train_no,"platform":platform,
                 "depart_name": depart_name, "depart_code": depart_code, "depart_city_code": depart_city_code,
                 "arrive_name": arrive_name, "arrive_code": arrive_code, "arrive_city_code": arrive_city_code,
                 "name": name, "card_type": card_type, "card_no": card_no, "phone": phone, "seat_name": seat_name,
                 "ticket_type": ticket_type, "status": status, "price": price , "create_time": create_time}


            dict_list.append(t)
            # conf.order.insert(t)
        except Exception as e:
            error_file.write(line)

        if count % 10000 == 0 or (count == (file_lines-1)):
            # print dict_list
            print (file_in_path, str(count))
            db.sub_order.insert(dict_list)
            dict_list = []

def main():
    # file_name_list =["user_sub_order_test.txt"]
    file_name_list = ["uoaa", "uoab", "uoac", "uoad", "uoae", "uoaf", "uoag",
                       "uoah", "uoai", "uoaj", "uoak", "uoal", "uoam", "uoan",
                        "uoao", "uoap", "uoaq", "uoar", "uoas", "uoat",
                         "uoau", "uoav", "uoaw", "uoax", "uoay", "uoaz",
                          "uoba", "uobb", "uobc", "uobd"]

    file_name_list =["user_sub_order_test.txt"]
    file_name_list =["user_sub_order20150104.txt"]
    error_file_name = "sub_error_new.log"

    file_list_path,err_path = get_file_list(file_name_list, error_file_name)
    for file_name in file_list_path:
        print file_name
        data_in(file_name,err_path,"169server")
    print len(file_list_path)
if __name__ == "__main__":
    # data_in(file_in_path, error_path, "")
    main()
    pass
