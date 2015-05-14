#coding=utf-8
__author__ = 'Administrator'
import model
import file_search
def txt_split(txt_path):
    #从数据库查询的txt分出每天，分平台的txt
    list_temp = []
    file_in = open(txt_path)
    output_folder = "G:/data/89everydayout2/"
    i = 0
    for line in file_in:
        stringArr = line.strip().split("\t")
        uid = stringArr[0]
        p_info = stringArr[1]
        create_time = stringArr[2]
        os_state = ""
        if "ios" in p_info:
            os_state = "ios"
        else:
            os_state = "android"

        result_out_path = output_folder + create_time + "_" + os_state
        result_output = open(result_out_path,"a")

        result_output.write(line)
        i += 1
        print(i)

def getFilePathList(file_folder):
    #输入目录，搜索所有文件，返回文件路径list
    file_path_list = []

    file_list = file_search.get_all_file(file_folder)
    for file in file_list:
        file_path_list.append(file)
        # print(file)
    return file_path_list

def get_uid(txt_path):
    file_in = open(txt_path)
    file_name = txt_path.strip().split("/")

    print(file_name[-1])
    output_folder = "G:/data/89everydayuid/"
    result_out_path = output_folder+file_name[-1]
    print(result_out_path)
    result_output = open(result_out_path,"a")
    for line in file_in:
        stringArr = line.strip().split("\t")
        uid = stringArr[0]
        p_info = stringArr[1]
        create_time = stringArr[2]
        result_output.write(uid+"\n")


def test_getUid():
    test_path = "G:/data/gt_uid/test.txt"

    path89 = "G:/data/89data/89retult.txt"

    txt_folder = "G:/data/89everydayout3"
    # getTxtList(path89)
    file_list = getFilePathList(txt_folder)
    for file_path in file_list:
        get_uid(file_path)
    # print(file_list)
    pass


if __name__ == '__main__':
    txt_in="G:/data/89data/result0309.txt"
    # txt_split(txt_in)
    test_getUid()
    pass