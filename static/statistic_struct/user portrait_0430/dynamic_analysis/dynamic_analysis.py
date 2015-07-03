#ecoding=utf-8
__author__ = 'Administrator'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime
import time
from collections import defaultdict

def str_to_datetime(str):
    try:
        out_date_time = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
    except Exception as e:
        out_date_time = None
    return out_date_time

def datetime_differ_seconds(datetime1, datetime2):
    if date_time_1 is None or date_time_2 is None:
        return -1
    else:
        seconds_differ = (datetime1 - datetime2).seconds
        return seconds_differ


def get_Data():
    file_in_path = "data/out_data.dat"
    file_in = open(file_in_path)

    data_dict = defaultdict(list)

    for line in file_in:

        stringArr = line.strip().split("\t")

        record_is = stringArr[0]
        flyno = stringArr[1]
        depcode = stringArr[2]
        arrcode = stringArr[3]
        flydate = stringArr[4]
        old_state = stringArr[5]#.encode('gbk')
        new_state = stringArr[6]#.encode('utf-8')
        data_source = stringArr[7]
        oper_type = stringArr[8]
        operid = stringArr[9]
        is_send = stringArr[10]


        createtime = str_to_datetime(stringArr[11])
        updatetime = str_to_datetime(stringArr[12])

        remark = stringArr[13]
        update_reason = stringArr[14]

        old_depplan = str_to_datetime(stringArr[15])
        old_arrplan = str_to_datetime(stringArr[16])
        old_depready = str_to_datetime(stringArr[17])
        old_arrready = str_to_datetime(stringArr[18])
        old_deptime = str_to_datetime(stringArr[19])
        old_arrtime = str_to_datetime(stringArr[20])

        new_depplan = str_to_datetime(stringArr[21])
        new_arrplan = str_to_datetime(stringArr[22])
        new_depready = str_to_datetime(stringArr[23])
        new_arrready = str_to_datetime(stringArr[24])
        new_deptime = str_to_datetime(stringArr[25])
        new_arrtime = str_to_datetime(stringArr[26])

        laterno = stringArr[27]
        laterdep = stringArr[28]
        laterarr = stringArr[29]
        stop = stringArr[30]
        mark = stringArr[31]
        fs_share = stringArr[32]

        data_dict[flyno].append((old_state, new_state, createtime, updatetime,
                                 old_depplan, new_depplan, old_arrplan, new_arrplan,
                                 old_depready, new_depready, old_arrready, new_arrready,
                                 old_deptime, new_deptime, old_arrtime, new_arrtime
        ))

    # print(len(data_dict))
    data_dict_out = defaultdict(set)
    for k, values in data_dict.items():
        value_set = set(values)
        data_dict_out[k] = value_set

    return data_dict_out
        # print(k,len(values), len(set(values)), values)
    # print(data_dict)


def simple_analysis(data_dict):
    i = 0

    total_statistics_dict = defaultdict(list)


    for k, values in data_dict.items():
        # print(k,values)
        for value in values:
            # print(value)
            (old_state, new_state, createtime, updatetime,
            old_depplan, new_depplan, old_arrplan, new_arrplan,
            old_depready, new_depready, old_arrready, new_arrready,
            old_deptime, new_deptime, old_arrtime, new_arrtime) = value
            # print(old_state, new_state,"计划", "起飞")
            # if old_state == "计划" and new_state == "起飞":
            #     i += 1
            # total_statistics_dict[str(old_state.encode("utf-8") + "," + new_state.encode("utf-8"))].append(1)

    for k, value in total_statistics_dict.items():
        print(k, len(value))
    # return i



if __name__ == "__main__":
    # get_Data()
    name = "到达"
    print("到达", name.encode('gbk'))
    # print("武汉")

    date_time_str1 = '2015-06-30 08:23:49'
    date_time_1 = datetime.datetime.strptime(date_time_str1, "%Y-%m-%d %H:%M:%S")


    date_time_str2 = '2015-06-30 10:23:49'
    date_time_2 = datetime.datetime.strptime(date_time_str2, "%Y-%m-%d %H:%M:%S")

    print((date_time_2 - date_time_1), (date_time_2 - date_time_1).seconds, type(date_time_2 - date_time_1))


    # date_time_2 = time.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
    print(date_time_1)
    data_dict_out = get_Data()
    i = simple_analysis(data_dict_out)

    print()
    print("计划","jihua")
    print("起飞","qifei")
    print("到达","daoda")
    print("返航","fanhang")
    print("取消","quxiao")
    print("备降","beijiang")
    print("延误","yanwu")
    pass



