__author__ = 'Administrator'
import time
from collections import Counter
from collections import OrderedDict
from mongo import gt_source_dao
from db import source_dao

def get_phone_dict():
    o_PhoneDict = source_dao.PhoneDictDao()
    dict_city, dict_sheng = o_PhoneDict.get_phone_dict()
    # print(dict_city)
    return dict_city
    pass

def gt_exchange(user_list):
    print("gt_exchange_start:" + str(time.ctime()))
    phone_city_list = []
    idcard_list_male = []
    idcard_list_female = []

    phone_dict = OrderedDict(sorted(get_phone_dict().items(), key=lambda t:t[0]))
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
                    print(cardno)

        except Exception as e:
            pass
    print("gt_exchange_end:" + str(time.ctime()))
    return phone_city_list, idcard_list_male, idcard_list_female


def out_count(result_list, out_file_path):
    out_file = open(out_file_path, "a")
    result = Counter(result_list)
    result_dict = dict(result)
    for (key, value) in result_dict.items():
        out_file.write(str(key) + "\t" + str(value) + "\n")
        # print (str(key) + str(value))
    # print(result)
    pass



if __name__ == "__main__":
    # o_OrderPhoneDao = source_dao.OrderPhoneDao()
    # result = o_OrderPhoneDao.get_user_identity()
    print("start:" + str(time.ctime()))
    print("getMondoData_start:" + str(time.ctime()))


    result = gt_source_dao.getMondoData()
    phone_city_list,idcard_list_male, idcard_list_female = gt_exchange(result)

    out_count(phone_city_list, "hb_city.data")
    out_count(idcard_list_male, "gt_male_age.data")
    out_count(idcard_list_female, "gt_female_age.data")

    pass

