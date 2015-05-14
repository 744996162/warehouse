__author__ = 'Administrator'

from collections import Counter


arr_city_path = "G:/data/gt0402/arr/"
dep_city_path = "G:/data/gt0402/dep/"
uid_path = "G:/data/gt0402/uid/"

arr_out_path = "G:/data/gt0402/arrresult/"
dep_out_path = "G:/data/gt0402/depresult/"

month_list = ["08", "09", "10", "11", "12"]
file_out_list = ["08", "09", "10", "11", "12"]

def getTxtList(txt_path):

    list_temp = []
    file_in = open(txt_path)
    for line in file_in:
        stringArr = line.strip().split("\n")
        list_temp.append(stringArr[0])
    # print(list)
    # list_result = list(set(list_temp))
    # print(len(list_result))
    return list_temp



def city_static():
    file_count = 0

    for i in month_list:
        # file_open = open(arr_city_path+i)
        # cou = 0
        list_temp = getTxtList(dep_city_path + i)
        count_result_file = open(dep_out_path + file_out_list[file_count], "a")
        cnt = Counter(list_temp)
        temp_count = 0
        for k, v in cnt.iteritems():
            string_out = str(k) + "\t" + str(v)
            count_result_file.write(string_out + "\n")
            temp_count += 1
            if temp_count % 10000 == 0:
                print(temp_count)
        file_count += 1

if __name__ == "__main__":
    city_static()