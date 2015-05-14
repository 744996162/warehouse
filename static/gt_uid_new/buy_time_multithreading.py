#coding=utf-8
__author__ = 'Administrator'
import file_search
from collections import Counter

def cal89():
    file_path = "G:/data/89data/89his_1218.txt"
    result_path = "G:/data/gt_order_uid/89_201412.txt"
    file_in = open(file_path)
    file_out = open(result_path, "a")
    for line in file_in:
        string_arr = line.strip().split("\t")
        # print(string_arr)
        uid = string_arr[0]
        # p_info = string_arr[1]
        create_time = string_arr[2]
        # print(line)
        if int(create_time) < 20150101:
            file_out.write(uid+"\n")
    # file_out.close()
    pass

def cal89_ios_break():
    file_path = "G:/data/89data/89his_1218.txt"
    result_path = "data0319/ios_break/89his_201412.txt"
    file_in = open(file_path)
    file_out = open(result_path, "a")
    for line in file_in:
        string_arr = line.strip().split("\t")
        # print(string_arr)
        uid = string_arr[0]
        # p_info = string_arr[1]
        create_time = string_arr[2]
        # print(line)
        if (int(create_time) < 20150101) and (uid == "20c27fb772000217b"):
            file_out.write(uid+"\n")
    # file_out.close()
    pass
    pass

def line_count(file_path):
    num_lines = sum(1 for line in open(str(file_path)))
    return num_lines


def get_file_list():
    folder = "G:/data/gt_order_uid/new"
    file_list = file_search.get_all_file(folder)
    for file_temp in file_list:
        # print(file_temp, str(line_count(file_temp)))
        pass
    return file_list

def getTxtList(txt_path):
    #获取txt里面uid的list
    list_temp = []
    file_in = open(txt_path)
    for line in file_in:
        stringArr = line.strip().split("\n")
        list_temp.append(stringArr[0])
    # print(list)
    # list_result = list(set(list_temp))
    # print(len(list_result))
    return list_temp

def get_all_uid():
    file_test = "G:/data/gt_order_uid/new/201401.txt"
    file_name_list = get_file_list()
    uid_all_list = []
    for file in file_name_list:
        uid_list = getTxtList(file)
        print(len(uid_list))
        uid_all_list += uid_list
    return uid_all_list

    # listMerge()
    # uid_list = getTxtList(file_test)
    # uid_list_set = list(set(uid_list))
    # print(len(uid_list_set))
    # pass

def test_get_uid_count():
    result_path = "G:/data/gt_order_uid/result/"
    uid_path = result_path+"uid_count.txt"
    count_path = result_path+"count_list.txt"

    uid_out = open(uid_path,"a")
    count_out = open(count_path,"a")

    uid_all_list = get_all_uid()
    uid_all_set = set(uid_all_list)
    print(len(uid_all_set))

    temp_count = 0

    for item in uid_all_set:
        uid_count = uid_all_list.count(item)
        string_out = str(item) + "\t" + str(uid_count)

        uid_out.write(string_out + "\n")
        count_out.write(str(uid_count) + "\n")
        temp_count += 1
        if temp_count % 1000 == 0:
            print(temp_count)

    pass

def get_uid_count():
    file_in_path = "G:/data/gt_order_uid/new/all.txt"
    # file_in_path_test = "G:/data/gt_order_uid/new/201401.txt"
    file_in_path_ios_break = "G:/data/gt_order_uid/result/ios_break/ios_break.txt"

    result_path = "G:/data/gt_order_uid/result/"
    uid_path = result_path+"uid_count_ios_break.txt"
    count_path = result_path+"count_list_ios_break.txt"

    uid_out = open(uid_path, "a")
    count_out = open(count_path, "a")

    uid_all_list = getTxtList(file_in_path_ios_break)

    # uid_all_set = set(uid_all_list)
    # print(len(uid_all_set))
    #
    temp_count = 0

    cnt = Counter(uid_all_list)
    #
    for k, v in cnt.iteritems():
        string_out = str(k) + "\t" + str(v)
        uid_out.write(string_out + "\n")
        count_out.write(str(v) + "\n")
        temp_count += 1
        if temp_count % 10000 == 0:
            print(temp_count)

    # for item in uid_all_set:
    #     uid_count = uid_all_list.count(item)
    #     string_out = str(item) + "\t" + str(uid_count)
    #
    #     uid_out.write(string_out + "\n")
    #     count_out.write(str(uid_count) + "\n")
    #     temp_count += 1
    #     if temp_count % 1000 == 0:
    #         print(temp_count)
    #
    # pass

def count_result():
    count_path = "G:/data/gt_order_uid/result/count_list(cotain_ios_break)"
    count_list = getTxtList(count_path)
    print(len(count_list))

    result_path = "G:/data/gt_order_uid/result/"
    count_result_path = result_path+"result(cotain_ios_break)"
    count_result_file = open(count_result_path, "a")

    temp_count = 0
    cnt = Counter(count_list)


    for k, v in cnt.iteritems():
        string_out = str(k) + "\t" + str(v)
        count_result_file.write(string_out + "\n")
        temp_count += 1
        if temp_count % 10000 == 0:
            print(temp_count)

    pass

if __name__ == "__main__":
    # cal89()
    #print(get_file_list())

    # get_file_list()
    # result_path = "G:/data/gt_order_uid/result/"
    # list_all = get_all_uid()
    # print(len(list_all))

    # get_uid_count()
    count_result()
    # cal89_ios_break()