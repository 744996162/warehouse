#coding=utf-8
__author__ = 'Administrator'
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
        stringArr=line.strip().split("\n")
        list_temp.append(stringArr[0])
    # print(list)
    list_result = list(set(list_temp))
    print(len(list_result))
    return list_result


def listMerge():
    file_path_list = getFilePathList()
    list_result = []
    for file_path in file_path_list:
        list_temp = getTxtList(file_path)
        list_result += list_temp
    list_result_out = list(set(list_result))
    print(len(list_result_out))
    return list_result_out

def list_to_txt(_list,_txt_path):
    result_output=open(_txt_path,'w')
    for temp in _list:
        result_output.write(temp+'\n')
    pass

def quCong(_list):
    list_result = list(set(_list))
    return list_result

if __name__ == "__main__":
    # list_all = listMerge()
    # list_result = quCong(list_all)
    # print(len(list_result))

    list_102_1227=listMerge()

    list_to_txt(list_102_1227,"G:/data/test/list_102_1227")