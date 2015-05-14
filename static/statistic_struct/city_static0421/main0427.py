#ecoding=utf-8
__author__ = 'Administrator'
from collections import Counter
from source_dao0427 import PhoneDictDao
from source_dao0427 import OrderPhoneDao
from source_dao0427 import CodeDictDao

def get_phone_dict():
    o_PhoneDict = PhoneDictDao()
    dict_city, dict_sheng = o_PhoneDict.get_phone_dict()
    return dict_city
    pass

def get_code_dict():
    o_CodeDict = CodeDictDao()
    dict_code = o_CodeDict.get_code_dict()
    return dict_code

#得到所有注册用户手机号
def get_all_phone(file_in_path):
    # file_in = open("data/orderphone_0413to0426.data")
    file_in = open(file_in_path)
    phone_info_list = []
    for i in file_in:
        phone_info_list.append(i)
    print(len(phone_info_list))
    return phone_info_list


def get_order_cityname(all_phone_info_list, phone_dict, out_file_path=""):
    if out_file_path != "":
        out_file = open(out_file_path, "a")
    city_name_list = []

    for phone_info in all_phone_info_list:
        stringArr = phone_info.strip().split('\t')

        flyno = stringArr[0]
        depcode = stringArr[1]
        arrcode = stringArr[2]
        phone = stringArr[3]
        phoneid = stringArr[4]

        phone_temp = phone[0:7]
        # print(phone_temp)
        try:
            city_name = phone_dict[str(phone_temp)]
        except Exception as e:
            print(e)
            print(phone)
            city_name = "NULL"
        city_name_list.append(city_name)
        if out_file_path != "":
            out_file.write(phone + "\t" + city_name + "\n")
    return city_name_list

def get_order_departcode(all_phone_info_list, dict_code, out_file_path=""):
    if out_file_path != "":
        out_file = open(out_file_path, "a")
    city_name_list = []
    for phone_info in all_phone_info_list:
        stringArr = phone_info.strip().split('\t')

        flyno = stringArr[0]
        depcode = stringArr[1]
        arrcode = stringArr[2]
        phone = stringArr[3]
        phoneid = stringArr[4]
        phone_temp = phone[0:7]

        try:
            city_name = dict_code[str(depcode)]
        except Exception as e:
            print(e)
            print(depcode)
            city_name = "NULL"
        city_name_list.append(city_name)
        if out_file_path != "":
            out_file.write(phone + "\t" + city_name + "\n")
    return city_name_list



def countCity(city_name_list, file_out_path="city_count0427.data"):
    file_out = open(file_out_path, "a")
    a = Counter(city_name_list)
    for key in a.keys():
        file_out.write(str(key) + "\t" + str(a.get(key)) + "\n")
        print(key, a.get(key))
    pass


# def test_main():
#     all_phone_info_list = get_all_phone()
#     dict_city = get_phone_dict()
#     get_order_cityname_txt(all_phone_info_list, dict_city, out_file_path="order_result0427.data")
#     pass


def main(s_day, end_day, data_path_store, statics_path_out):
    # o_orderPhoneDao = OrderPhoneDao()
    # o_orderPhoneDao.result_to_txt(s_day, end_day, data_path_store)
    phone_info_list = get_all_phone(data_path_store)
    dict_city = get_phone_dict()
    city_name_list = get_order_cityname(phone_info_list, dict_city)
    countCity(city_name_list, statics_path_out)
    pass

def main2(data_path_store, statics_path_out):
    phone_info_list = get_all_phone(data_path_store)
    dict_code = get_code_dict()
    depart_code_list = get_order_departcode(phone_info_list, dict_code)
    countCity(depart_code_list, statics_path_out)
    pass

    pass


if __name__ == "__main__":
    # main("2015-05-01", "2015-05-03", "data/order_phone_0501_0503.data", "count_result_0501_0503.data")
    main2("data/order_phone_0501_0503.data", "count_departcode_0501_0503name.data")
    pass
