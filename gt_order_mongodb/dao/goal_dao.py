__author__ = 'Administrator'
import pymongo
import datetime
from tools.getCityCode import CityCode
import logging

class InsertData():
    def __init__(self, dbtype="169server"):
        self.dbtype = dbtype
        self.o_city_code = CityCode()
        pass

    def _getCon(self, dbtype):
        if dbtype == "169server":
            con_local = pymongo.Connection(host="localhost", port=27017)
            db = con_local.admin
            db.authenticate("gtgj", "gtgj")
            db = con_local.gtgj
        else:
            con_local = pymongo.Connection(host="localhost", port=27017)
            db = con_local.gtgj
        return db

    def _stringToOrderJson(self, stringArr):
        t = {}
        # o_city_code = CityCode()
        try:
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

            depart_code = self.o_city_code.getStationCode(depart_name)
            depart_city_code = self.o_city_code.getCityCode(depart_name)
            arrive_code = self.o_city_code.getStationCode(arrive_name)
            arrive_city_code = self.o_city_code.getCityCode(arrive_name)

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
        except Exception as e:
            print(e)
            logging.error(e)

        return t



    def _stringToSubOrderJson(self, stringArr):
        t = {}
        try:
            t = {}
            order_id = stringArr[0]
            t["order_id"] = order_id
            uid = stringArr[1]
            t["uid"] = uid

            account = stringArr[2]
            t["account"] = account

            p_info = stringArr[3]
            t["p_info"] = p_info

            if "ios" in p_info:
                platform = "ios"
            else:
                platform = "android"
            t["platform"] = platform

            depart_date = stringArr[4]
            try:
                i_depart_date = int(depart_date[0:4]+depart_date[5:7]+depart_date[8:10])
                t["depart_date"] = i_depart_date
            except Exception as e:
                pass

            train_no = stringArr[5]
            t["train_no"] = train_no

            depart_name = stringArr[6]
            arrive_name = stringArr[7]

            depart_code = self.o_city_code.getStationCode(depart_name)
            depart_city_code = self.o_city_code.getCityCode(depart_name)
            arrive_code = self.o_city_code.getStationCode(arrive_name)
            arrive_city_code = self.o_city_code.getCityCode(arrive_name)

            t["depart_code"] = depart_code
            t["depart_city_code"] = depart_city_code
            t["arrive_code"] = arrive_code
            t["arrive_city_code"] = arrive_city_code

            name = stringArr[8]
            t["name"] = name

            card_type = stringArr[9]
            t["card_type"] = card_type

            card_no = stringArr[10]
            t["card_no"] = card_no

            phone = stringArr[11]
            t["phone"] = phone

            seat_name = stringArr[12]
            t["seat_name"] = seat_name

            ticket_type = stringArr[13]
            t["ticket_type"] = ticket_type

            status = stringArr[14]
            t["status"] = status

            price = float(stringArr[15])
            t["price"] = price

            create_time = datetime.datetime.strptime(stringArr[16], "%Y-%m-%d %H:%M:%S")
            t["create_time"] = create_time

            try:
                t["order_date"] = int(create_time.strftime("%Y%m%d"))
            except Exception as e:
                pass
        except Exception as e:
            logging.error(e)
            # print(e)

        return t

        pass


    #filetype = "order" or "order_his"
    def orderFileInsert(self, file_in_path, file_type="order"):
        file_in = open(file_in_path)

        file_lines = len(file_in.readlines())
        file_in = open(file_in_path)

        db = self._getCon(self.dbtype)

        dict_list = []

        for (count, line) in enumerate(file_in):
            stringArr = line.strip().split("\t")
            t = self._stringToOrderJson(stringArr)
            if t != {} or (len(t) > 0):
                dict_list.append(t)

            if count % 10000 == 9999 or (count == (file_lines-1)):
                logging.info(file_in_path, str(count+1))
                print(file_in_path, str(count+1))
                if file_type == "order" or file_type == "":
                    db.order.insert(dict_list)
                elif file_type == "order_his" or file_type == "order_history":
                    db.order_history.insert(dict_list)
                else:
                    break
                dict_list = []
        pass

    #filetype = "sub_order" or "sub_order_his"
    def subOrderFileInsert(self, file_in_path, file_type="sub_order"):
        file_in = open(file_in_path)
        file_lines = len(file_in.readlines())
        file_lines = len(file_in.readlines())
        file_in = open(file_in_path)

        db = self._getCon(self.dbtype)
        dict_list = []

        for (count, line) in enumerate(file_in):
            stringArr = line.strip().split("\t")
            t = self._stringToSubOrderJson(stringArr)

            if t != {} or (len(t) > 0):
                dict_list.append(t)

            if count % 10000 == 9999 or (count == (file_lines-1)):
                logging.info(file_in_path, str(count+1))
                print(file_in_path, str(count+1))

                if file_type == "sub_order" or file_type == "":
                    db.sub_order.insert(dict_list)

                elif file_type == "sub_order_his" or file_type == "sub_order_history":
                    db.sub_order_history.insert(dict_list)
                dict_list = []



if __name__ == "__main__":
    o_insertData = InsertData(dbtype="local")
    o_insertData.orderFileInsert("G:/user_order_20150419_20150422")

    pass

