#ecoding=utf-8
__author__ = 'Administrator'
import pymongo
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
station_info_path = "station_info.txt"
station_info_file = open(station_info_path)




def con():

    con_225=pymongo.Connection(host="182.92.194.225", port=27017)
    db = con_225.collectdata
    db.authenticate("readonly", "read@hl123")
    # flight=conf.flight_price_percent.find()
    flight = db.flight_price_percent.find({"datatime": {"$gt":date_start, "$lt":date_end}})

def getJson():
    # stringArr = line.strip().split("\t")
    stringArr = ""
    uid = stringArr[0]
    p_info = stringArr[1]
    account = stringArr[2]
    order_date = stringArr[3]
    s_order_date = order_date[0:4]+order_date[5:7]+order_date[8:10]
    i_order_date = int(s_order_date)
    i_status = int(stringArr[4])
    depart_date = stringArr[5]
    depart_name = stringArr[6]
    arrive_name = stringArr[7]
    ticket_count = stringArr[8]
    train_no = stringArr[9]
    amount = stringArr[10]
    create_time = stringArr[11]


    t = {"uid": uid, "p_info": p_info, "account": account, "order_date": i_order_date,
         "i_status": i_status, "depart_date": depart_date, "depart_name": depart_name, "arrive_name": arrive_name,
         "ticket_count": ticket_count, "train_no": train_no, "amount": amount, "create_time": create_time}

    pass


dict_code={}
dict_city_code={}
for line in station_info_file:
    stringArr=line.strip().split("\t")
    code = stringArr[0]
    name = stringArr[1].encode('gbk')
    # print name.decode('gbk').encode('utf-8')
    # print name.encode('gbk').encode('utf-8')
    # print name.decode('utf-8')
    # print(name.decode('utf-8'))
    city_code = stringArr[2]
    dict_code.setdefault(name, code)
    dict_city_code.setdefault(name, city_code)
        # print(code, name, city_code)

# print dict_code


def getCode(name="北京"):
    code = dict_code.get(name)
    city_code = dict_city_code.get(name)
    # print(code,city_code)
    return code, city_code

if __name__=="__main__":
    # getCityCode()
    print(getCode('\xc9\xe1\xc1\xa6\xbb\xa2'))