__author__ = 'Administrator'

import time
from collections import Counter
from collections import OrderedDict
from mongo import gt_source_dao0518
from db import source_dao

def get_static(cardno_list):
    print("gt_start:" + str(time.ctime()))
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


def gt_main(s1,s2):
    result_model_list = gt_source_dao0518.getMondoData2015(s1, s2, "169server")
    age_list_male, age_list_female, age_set_male, age_set_female = get_static(result_model_list)
    print(len(age_list_male))
    print(len(age_set_male))
    base_file_name = "data0518/" + str(s1)
    out_count(age_list_male, base_file_name + "gt_list_male.data")
    out_count(age_list_female, base_file_name + "gt_list_female.data")
    out_count(age_set_male, base_file_name + "gt_set_male.data")
    out_count(age_set_female, base_file_name +"gt_set_female.data")
    pass

if __name__ == "__main__":
    gt_main(20150101,20150401)