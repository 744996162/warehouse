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

def getTxtList(txt_path):
    #获取txt里面uid的list
    list_temp = []
    file_in = open(txt_path)
    for line in file_in:
        stringArr = line.strip().split("\n")
        list_temp.append(stringArr[0])
    # print(list)
    list_result = list(set(list_temp))
    # print(len(list_result))
    return list_result

def listMerge(*arg):

    list_result = []
    for list_temp in arg:
        list_result += list_temp
    list_result_out = list(set(list_result))
    return list_result_out
