#ecoding=utf-8
__author__ = 'Administrator'
import pandas
from source_dao import PhoneDict


def query_city_phone_dict(city_name):
    o_phoneDict = PhoneDict()
    phone_result = []
    phone_model_list = o_phoneDict.get_phoneDict(city_name)
    for phone_model in phone_model_list:
        phone_result.append(phone_model.phone)

    phone_result_set = set(phone_result)
    print(len(phone_result_set))
    return phone_result_set

#得到所有注册用户手机号
def get_all_phone():
    file_in = open("data/phone_result0422.data")
    phone_info_list = []
    for i in file_in:
        phone_info_list.append(i)
    print(len(phone_info_list))
    return phone_info_list
    pass


def get_city_phone(all_phone_info_list, city_phone_dict):

    result_city_phone_list = []

    for phone_info in all_phone_info_list:
        stringArr = phone_info.strip().split('\t')

        phone = stringArr[0]
        phoneid = stringArr[1]

        phone_temp = phone[0:7]
        # print(phone_temp)
        if phone_temp in city_phone_dict:
            result_city_phone_list.append(phone+"\t"+phoneid)
    return result_city_phone_list

def write_out(city_phone_list,city_name, out_file_path):
    out_file = open(out_file_path, "a")
    for city_phone in city_phone_list:
        out_file.write(city_phone + "\t" + city_name + "\n")
    return out_file_path


def test1():
    # 西安、珠海、徐州、桂林、济南、南昌、海口、呼和浩特
    city_dict = ["西安", "珠海", "徐州", "桂林", "济南", "南昌", "海口", "呼和浩特"]



def main(city_name, file_name, out_path="data/"):
    city_phone_dict = query_city_phone_dict(city_name)
    all_phone = get_all_phone()
    city_phone_list = get_city_phone(all_phone, city_phone_dict)
    file_name = file_name
    out_file = out_path + file_name

    write_out(city_phone_list, file_name, out_file)
    pass

def test_query_city_phone():
    result_set = query_city_phone_dict("西安")
    print(result_set)

    pass


if __name__ == "__main__":
    # test_query_city_phone()
    city_dict = ["西安", "珠海", "徐州", "桂林", "济南", "南昌", "海口", "呼和浩特"]
    name_dict = ["xian", "zhuhai", "xuzhou", "guilin", "jinan", "nancang", "haikou", "huhehaote"]
    for num, value in enumerate(city_dict):
        city_name = city_dict[num]
        file_name = name_dict[num]
        main(city_name,file_name)
        print city_name, file_name
    # main("西安","xian")
    # print("hello")