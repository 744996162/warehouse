#coding=utf-8
__author__ = 'Administrator'
import file_search

def getFilePathList():
    datapath = "G:/data/gt_uid/"
    file_path_list = []

    file_list = file_search.get_all_file(datapath)
    for file in file_list:
        file_path_list.append(file)
        # print(file)
    return file_path_list

def getTxtList(txt_path):
    #获取txt里面uid的list
    list = []
    file_in = open(txt_path)
    for line in file_in:
        stringArr = line.strip().split("\n")
        list.append(stringArr[0])
    # print(list)
    return list
    pass

def listMerge():
    file_path_list = getFilePathList()
    list = []
    for file_path in file_path_list:
        list_temp = getTxtList(file_path)
        list += list_temp
    print(len(list))
    return list

def quCong(_list):
    list_result = list(set(_list))
    return list_result

if __name__ == "__main__":
    list_all = listMerge()
    list_result = quCong(list_all)
    print(len(list_result))
