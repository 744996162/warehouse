#coding=utf-8
__author__ = 'Administrator'
from new_consumers_cal import *
from collections import Counter
from collections import OrderedDict

def cal1():
    base_path = "G:/data/gt0402/uid/"

    file_his_path =base_path + "102his.txt"
    file_08_path = base_path + "08"
    file_09_path = base_path + "09"
    file_10_path = base_path + "10"
    file_11_path = base_path + "11"
    file_12_path = base_path + "12"

    file_09new_path = open(base_path + "newconsumers/" + "09", "a")
    file_10new_path = open(base_path + "newconsumers/" + "10", "a")
    file_11new_path = open(base_path + "newconsumers/" + "11", "a")
    file_12new_path = open(base_path + "newconsumers/" + "12", "a")


    list_his = getTxtSetList(file_his_path)
    list_08 = getTxtSetList(file_08_path)
    list_09 = getTxtSetList(file_09_path)
    list_10 = getTxtSetList(file_10_path)
    list_11 = getTxtSetList(file_11_path)
    list_12 = getTxtSetList(file_12_path)

    list_his = set(listMerge(list_his, list_08))
    print(len(list_his))
    for i in list_09:
        if i not in list_his:
            file_09new_path.write(i+"\n")

    list_his = set(listMerge(list_his, list_09))
    for i in list_10:
        if i not in list_his:
            file_10new_path.write(i+"\n")
    print(len(list_his))

    list_his = set(listMerge(list_his, list_10))
    for i in list_11:
        if i not in list_his:
            file_11new_path.write(i+"\n")
    print(len(list_his))

    list_his = set(listMerge(list_his, list_11))
    for i in list_12:
        if i not in list_his:
            file_12new_path.write(i+"\n")
    print(len(list_his))


def cal2():
    base_path = "G:/data/gt0402/uid/"
    base_newpath = base_path + "newconsumers/"
    base_newbuy = base_path + "newbuy/"

    file_09new_path = base_newpath + "09"
    file_10new_path = base_newpath + "10"
    file_11new_path = base_newpath + "11"
    file_12new_path = base_newpath + "12"

    file_09_path = base_path + "09"
    file_10_path = base_path + "10"
    file_11_path = base_path + "11"
    file_12_path = base_path + "12"
    file_201501_path = base_path + "201501"

    file_09newbuy_path = base_newbuy + "09/"
    file_10newbuy_path = base_newbuy + "10/"
    file_11newbuy_path = base_newbuy + "11/"
    file_12newbuy_path = base_newbuy + "12/"


    file_09new_list = getTxtList(file_09new_path)

    file_10 = open(file_09newbuy_path+"10", "a")
    file_11 = open(file_09newbuy_path+"11", "a")
    file_12 = open(file_09newbuy_path+"12", "a")


    base_buystatic_path = "G:/data/gt0402/uid/buystatic/"
    buystatic_09 = open(base_buystatic_path + "09", "a")
    buystatic_10 = open(base_buystatic_path + "10", "a")
    buystatic_11 = open(base_buystatic_path + "11", "a")
    buystatic_12 = open(base_buystatic_path + "12", "a")
    buystatic_201501 = open(base_buystatic_path + "201501", "a")

    cnt09 = Counter(getTxtList(file_09_path))
    cnt10 = Counter(getTxtList(file_10_path))
    cnt11 = Counter(getTxtList(file_11_path))
    cnt12 = Counter(getTxtList(file_12_path))
    cnt201501 = Counter(getTxtList(file_201501_path))

    for k, v in cnt09.iteritems():
        string_out = str(k) + "\t" + str(v)
        buystatic_09.write(string_out + "\n")

    # for k, v in cnt10.iteritems():
    #     string_out = str(k) + "\t" + str(v)
    #     buystatic_10.write(string_out + "\n")
    #
    # for k, v in cnt11.iteritems():
    #     string_out = str(k) + "\t" + str(v)
    #     buystatic_11.write(string_out + "\n")
    #
    # for k, v in cnt12.iteritems():
    #     string_out = str(k) + "\t" + str(v)
    #     buystatic_12.write(string_out + "\n")
    #
    # for k, v in cnt201501.iteritems():
    #     string_out = str(k) + "\t" + str(v)
    #     buystatic_201501.write(string_out + "\n")

    # for i in getTxtList(file_10_path):
    #     if i in file_09new_list:
    #         file_10.write(i + "\n")
    #
    # for i in getTxtList(file_11_path):
    #     if i in file_09new_list:
    #         file_10.write(i + "\n")
    #
    # for i in getTxtList(file_12_path):
    #     if i in file_09new_list:
    #         file_10.write(i + "\n")
    #
    # pass


def cal3():
    base_buystatic_path = "G:/data/gt0402/uid/buystatic/"
    buystatic_09 = open(base_buystatic_path + "09")
    buystatic_10 = open(base_buystatic_path + "10")
    buystatic_11 = open(base_buystatic_path + "11")
    buystatic_12 = open(base_buystatic_path + "12")
    buystatic_201501 = open(base_buystatic_path + "201501")

    base_path = "G:/data/gt0402/uid/"
    base_newpath = base_path + "newconsumers/"
    file_09new_path = base_newpath + "09"
    file_10new_path = base_newpath + "10"
    file_11new_path = base_newpath + "11"
    file_12new_path = base_newpath + "12"


    #新增消费用户后续购买行为
    base_newbuy = base_path + "newbuy/"
    file_09newbuy_path = base_newbuy + "09/"
    file_10newbuy_path = base_newbuy + "10/"
    file_11newbuy_path = base_newbuy + "11/"
    file_12newbuy_path = base_newbuy + "12/"
    file_10 = open(file_09newbuy_path+"10", "a")
    file_11 = open(file_09newbuy_path+"11", "a")
    file_12 = open(file_09newbuy_path+"12", "a")


    list09 = getTxtList(file_09new_path)

    for line in buystatic_09:
        stringArr = line.strip().split("\t")
        uid = stringArr[0]
        if uid in list09:
            file_10.write(line)

    # for line in buystatic_10:
    #     stringArr = line.strip().split("\t")
    #     uid = stringArr[0]
    #     if uid in list09:
    #         file_10.write(line)
    #
    # for line in buystatic_11:
    #     stringArr = line.strip().split("\t")
    #     uid = stringArr[0]
    #     if uid in list09:
    #         file_11.write(line)
    #
    # for line in buystatic_12:
    #     stringArr = line.strip().split("\t")
    #     uid = stringArr[0]
    #     if uid in list09:
    #         file_12.write(line)
    pass


def cal4():
    base_buystatic_path = "G:/data/gt0402/uid/buystatic/"
    buystatic_09 = open(base_buystatic_path + "09")
    buystatic_10 = open(base_buystatic_path + "10")
    buystatic_11 = open(base_buystatic_path + "11")
    buystatic_12 = open(base_buystatic_path + "12")
    buystatic_201501 = open(base_buystatic_path + "201501")

    base_path = "G:/data/gt0402/uid/"
    base_newpath = base_path + "newconsumers/"
    file_09new_path = base_newpath + "09"
    file_10new_path = base_newpath + "10"
    file_11new_path = base_newpath + "11"
    file_12new_path = base_newpath + "12"


    #新增消费用户后续购买行为
    base_newbuy = base_path + "newbuy/"
    file_09newbuy_path = base_newbuy + "09/"
    file_10newbuy_path = base_newbuy + "10/"
    file_11newbuy_path = base_newbuy + "11/"
    file_12newbuy_path = base_newbuy + "12/"
    # file_09 = open(file_12newbuy_path+"09", "a")
    file_10 = open(file_11newbuy_path+"10", "a")
    file_11 = open(file_11newbuy_path+"11", "a")
    file_12 = open(file_11newbuy_path+"12", "a")
    file_201501 = open(file_11newbuy_path+"201501", "a")

    # list09 = getTxtList(file_09new_path)
    list10 = getTxtList(file_11new_path)

    # d09 ={}
    # for line in buystatic_09:
    #     stringArr = line.strip().split("\t")
    #     uid = stringArr[0]
    #     value = stringArr[1]
    #     d09[uid] = value
    #
    # ordered_dict = OrderedDict(d09)
    # file_09 = open(file_09newbuy_path+"09", "a")
    # for i in list09:
    #     value = ordered_dict.get(i)
    #     if value is not None:
    #         file_09.write(i + "\t" + str(value) + "\n")

    # d10 ={}
    # for line in buystatic_10:
    #     stringArr = line.strip().split("\t")
    #     uid = stringArr[0]
    #     value = stringArr[1]
    #     d10[uid] = value
    #
    # ordered_dict = OrderedDict(d10)
    # file_10 = open(file_10newbuy_path+"10", "a")
    # for i in list10:
    #     value = ordered_dict.get(i)
    #     if value is not None:
    #         file_10.write(i + "\t" + str(value) + "\n")

    d11 ={}
    for line in buystatic_11:
        stringArr = line.strip().split("\t")
        uid = stringArr[0]
        value = stringArr[1]
        d11[uid] = value

    ordered_dict = OrderedDict(d11)
    for i in list10:
        value = ordered_dict.get(i)
        if value is not None:
            file_11.write(i + "\t" + str(value) + "\n")


    d12 ={}
    for line in buystatic_12:
        stringArr = line.strip().split("\t")
        uid = stringArr[0]
        value = stringArr[1]
        d12[uid] = value

    ordered_dict = OrderedDict(d12)
    for i in list10:
        value = ordered_dict.get(i)
        if value is not None:
            file_12.write(i + "\t" + str(value) + "\n")

    d201501 ={}
    for line in buystatic_201501:
        stringArr = line.strip().split("\t")
        uid = stringArr[0]
        value = stringArr[1]
        d201501[uid] = value

    ordered_dict = OrderedDict(d201501)
    for i in list10:
        value = ordered_dict.get(i)
        if value is not None:
            file_201501.write(i + "\t" + str(value) + "\n")


def cal5(file_in_path, file_out_path):
    file_in = open(file_in_path)
    file_out = open(file_out_path, "a")
    list_num = []
    for line in file_in:
        stringArr = line.strip().split("\t")
        uid = stringArr[0]
        value = stringArr[1]
        list_num.append(value)

    cnt_temp = Counter(list_num)

    for k, v in cnt_temp.iteritems():
        string_out = str(k) + "\t" + str(v)
        file_out.write(string_out + "\n")
    pass


if __name__ == "__main__":
    base_in_path = "G:/data/gt0402/uid/newbuy/"
    base_out_path = "G:/data/gt0402/uid/newbuystatic/"
    list_path = ["10/10", "10/11", "10/12", "10/201501", "11/11", "11/12", "11/201501", "12/12", "12/201501"]
    # list_path = ["09/09", "09/10", "09/11", "09/12", "10/10", "10/11", "10/12", "10/201501", "11/11", "11/12", "11/201501", "12/12", "12/201501"]
    # list_path = ["12/12", "12/201501"]
    for i in list_path:
        cal5(base_in_path+i, base_out_path+i)
    # cal4()