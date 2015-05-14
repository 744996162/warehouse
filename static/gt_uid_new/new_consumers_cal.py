#coding=utf-8
__author__ = 'Administrator'

import logging

import file_search

def getFilePathList(file_folder):
    #输入目录，搜索所有文件，返回文件路径list
    file_path_list = []

    file_list = file_search.get_all_file(file_folder)
    for file in file_list:
        file_path_list.append(file)
        # print(file)
    return file_path_list

def getTxtSetList(txt_path):
    #获取txt里面uid的list(去重后)
    list_temp = []
    file_in = open(txt_path)
    for line in file_in:
        stringArr = line.strip().split("\n")
        list_temp.append(stringArr[0])
    # print(list)
    list_result = list(set(list_temp))
    # print(len(list_result))
    return list_result

def getTxtList(txt_path):
    #获取txt里面uid的list
    list_temp = []
    file_in = open(txt_path)
    for line in file_in:
        stringArr = line.strip().split("\n")
        list_temp.append(stringArr[0])
    return list_temp


def listMerge(*arg):

    list_result = []
    for list_temp in arg:
        list_result += list_temp
    list_result_out = list(set(list_result))
    return list_result_out


def main():
    everday_file_folder = "G:/data/89everydayuid"
    his_file_path = "G:/data/test/102his_all.txt"
    result_out_path = "G:/data/test/result0309.txt"
    result_out_path2 ="G:/data/test/result_his_0308"
    his_list = getTxtList(his_file_path)

    everday_file_path_list = getFilePathList(everday_file_folder)

    # test_file_path = everday_file_path_list[0]
    for test_file_path in everday_file_path_list:
        test_file_list = getTxtList(test_file_path)

        his_consumers_count = len(his_list)
        consumers_count = len(test_file_list)
        test_file_name = test_file_path.strip().split("/")[-1]
        his_list = listMerge(his_list, test_file_list)
        his_consumers_new = len(his_list)
        new_consumers_count = his_consumers_new - his_consumers_count

        result_output = open(result_out_path, "a")

        print(test_file_name,"consumers_count:", consumers_count, "new_consumers_count:",new_consumers_count)
        result_output = open(result_out_path,"a")
        stringout = test_file_name + "\t" +"his_consumers_new"+ "\t" + str(his_consumers_new) + "\t" + "consumers_count:" + "\t" + str(consumers_count) + "\t" + "new_consumers_count:" + "\t" + str(new_consumers_count)+"\n"
        result_output.write(stringout)

    result_output2 = open(result_out_path2,"a")
    for i in his_list:
        result_output2.write(i+"\n")
    pass

if __name__ == '__main__':

    pass