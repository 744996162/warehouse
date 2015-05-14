#ecoding=utf-8
__author__ = 'Administrator'
from tools import *
import file_search
def cal_Q1():
    folder_path = "G:/data/89everydayconsumeruid/2015Q1"
    file_path_list = file_search.getAllFile(folder_path)

    android_file_path = []
    ios_file_path = []
    android_uid_list = []
    ios_uid_list = []


    for file_path in file_path_list:
        if "android" in file_path:
            android_file_path.append(file_path)
            uid_list_android = getTxtList(file_path)

            print(len(uid_list_android))
            android_uid_list += uid_list_android
            print(len(android_uid_list))

        else:
            ios_file_path.append(file_path)
            uid_list_ios = getTxtList(file_path)

            # print(len(uid_list_ios))
            ios_uid_list += uid_list_ios
            # print(len(ios_uid_list))

    # 活跃用户数:9393289 - 349,996 = 9043293

    android_set = set(android_uid_list)
    print("android:"+ str(len(android_set)))

    ios_set = set(ios_uid_list)
    print("ios:" + str(len(ios_set)))

def cal_2014gt_con():
    file_in = "G:/data/gt_order_uid/new/all.txt"
    list_2014 = getTxtList(file_in)
    list_set_2014 = set(list_2014)
    print(len(list_set_2014))

if __name__ == "__main__":
    cal_2014gt_con()