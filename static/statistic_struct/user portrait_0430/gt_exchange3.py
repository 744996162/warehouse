__author__ = 'Administrator'
import time
from collections import Counter
from collections import OrderedDict
from mongo import gt_source_dao3
from db import source_dao
import gc
import threading

def get_phone_dict():
    o_PhoneDict = source_dao.PhoneDictDao()
    dict_city, dict_sheng = o_PhoneDict.get_phone_dict()
    # print(dict_city)
    return dict_city
    pass

def gt_ex(user_list, phone_dict):
    print("gt_exchange_start:" + str(time.ctime()))
    phone_city_list = []
    idcard_list_male = []
    idcard_list_female = []

    # print(phone_dict)

    for user in user_list:

        phone = user.phone
        cardno = user.cardno
        phone_temp = phone[0:7]

        try:
            city_name = phone_dict[str(phone_temp)]
        except Exception as e:
            # print(e)
            # print(phone)
            city_name = "NULL"
        phone_city_list.append(city_name)

        try:
            if len(cardno) != 18:
                pass
            elif len(cardno) == 18:
                #4209841990
                # print(cardno)
                str_birth_year = cardno[6:10]
                gender = int(cardno[-2:-1])
                # print(cardno, str_birth_year,int(gender))

                age = 2015 - int(str_birth_year)
                if 0 <= age <= 100:
                    #female
                    if int(gender)%2 == 0:
                        idcard_list_female.append(age)
                        pass
                    #male
                    elif int(gender%2) == 1:
                        idcard_list_male.append(age)
                        pass
                else:
                    pass
                    # print(cardno)

        except Exception as e:
            pass
    print("gt_exchange_end:" + str(time.ctime()))
    return phone_city_list, idcard_list_male, idcard_list_female


def out_count(result_list, out_file_path):
    out_file = open(out_file_path, "a")
    c_result = Counter(result_list)
    result_dict = dict(c_result)
    for (key, value) in result_dict.items():
        out_file.write(str(key) + "\t" + str(value) + "\n")
        # print (str(key) + str(value))
    # print(result)
    return c_result


def count_to_txt(c_count,out_file_path):
    result_dict = dict(c_count)
    out_file = open(out_file_path, "a")
    for (key, value) in result_dict.items():
        out_file.write(str(key) + "\t" + str(value) + "\n")
    pass


if __name__ == "__main__":
    # o_OrderPhoneDao = source_dao.OrderPhoneDao()
    # result = o_OrderPhoneDao.get_user_identity()
    print("start:" + str(time.ctime()))
    print("getMondoData_start:" + str(time.ctime()))

    phone_dict = OrderedDict(sorted(get_phone_dict().items(), key=lambda t:t[0]))

    result_new2015 = gt_source_dao3.getMondoData_new()
    phone_city_list,idcard_list_male, idcard_list_female = gt_ex(result_new2015,phone_dict)
    out_count(phone_city_list, "hb_city_al.data")
    out_count(idcard_list_male, "gt_male_age_al.data")
    out_count(idcard_list_female, "gt_female_age_al.data")



    start_timelist = [20130101, 20140101, 20140201, 20140301, 20140401,20140501,20140601,20140701,20140801,20140901,20141001,20141101,20141201,20150101,20150201]
    end_timelist = [20140101, 20140201, 20140301, 20140401, 20140501,20140601,20140701,20140801,20140901,20141001,20141101,20141201,20150101,20150201,20150226]

    for count, value in enumerate(start_timelist):
        s_time = start_timelist[count]
        e_time = end_timelist[count]
        result = gt_source_dao3.getMondoData_old(s_time, e_time)
        phone_city_list,idcard_list_male, idcard_list_female = gt_ex(result,phone_dict)
        print(s_time, e_time)
        out_count(phone_city_list, "hb_city_al.data")
        out_count(idcard_list_male, "gt_male_age_al.data")
        out_count(idcard_list_female, "gt_female_age_al.data")
    pass

