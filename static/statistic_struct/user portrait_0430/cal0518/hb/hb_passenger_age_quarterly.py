__author__ = 'Administrator'

from db.hb_passenger_age_quarterly_dao import OrderPhoneDao
from domain import hb_model
import time
from collections import Counter

def hb_getCardNo(s1, s2):
    o_order = OrderPhoneDao()
    result_model_list = o_order.get_user_identity(s1, s2)
    cardno_list = []
    for model in result_model_list:
        cardno_list.append(model.cardno)

    age_list_male = []
    age_list_female = []
    age_set_male = []
    age_set_female = []

    for cardno in cardno_list:

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
                        age_list_female.append(age)
                        pass
                    #male
                    elif int(gender%2) == 1:
                        age_list_male.append(age)
                        pass
                else:
                    pass
                    # print(cardno)
        except Exception as e:
            pass
    # print("gt_end:" + str(time.ctime()))


    for cardno in set(cardno_list):

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
                        age_set_female.append(age)
                        pass
                    #male
                    elif int(gender%2) == 1:
                        age_set_male.append(age)
                        pass
                else:
                    pass
                    # print(cardno)
        except Exception as e:
            pass
    print("gt_end:" + str(time.ctime()))

    return age_list_male, age_list_female, age_set_male, age_set_female

def out_count(result_list, out_file_path):
    out_file = open(out_file_path, "a")
    c_result = Counter(result_list)
    result_dict = dict(c_result)
    for (key, value) in result_dict.items():
        out_file.write(str(key) + "\t" + str(value) + "\n")
        # print (str(key) + str(value))
    # print(result)
    return c_result

def hb_main(s1,s2):
    age_list_male, age_list_female, age_set_male, age_set_female = hb_getCardNo(s1,s2)
    print(len(age_list_male), len(age_set_male))
    print(len(age_set_male), len(age_set_female))

    base_file_name = "data/" + str(s1)
    out_count(age_list_male, base_file_name + "hb_list_male.data")
    out_count(age_list_female, base_file_name + "hb_list_female.data")
    out_count(age_set_male, base_file_name + "hb_set_male.data")
    out_count(age_set_female, base_file_name +"hb_set_female.data")
    pass


if __name__ == "__main__":
    hb_main("20130101", "20130401")
    hb_main("20130401", "20130701")
    hb_main("20130701", "20131001")
    hb_main("20131001", "20140101")

    hb_main("20140101", "20140401")
    hb_main("20140401", "20140701")
    hb_main("20140701", "20141001")
    hb_main("20141001", "20150101")

    hb_main("20150101", "20150401")

    pass



