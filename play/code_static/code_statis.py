#coding=utf-8
import os

def endWith(s, *endstring):
        array = map(s.endswith, endstring)
        if True in array:
            return True
        else:
            return False


#判断文件中是指定关键字结尾，是则将文件路径打印出来
def is_file_endwith(file_list, endstring=".py"):
    file_list_out = []
    for _file in file_list:
        if endWith(_file, endstring):
            file_list_out.append(_file)
            # print(_file)
    # print("Finish searching.")
    return file_list_out

#判断文件中是否包含关键字，是则将文件路径打印出来
def is_file_contain_word(file_list, query_word):
    file_list_out = []
    for _file in file_list:
        if query_word in open(_file).read():
            file_list_out.append(_file)
            # print(_file)
    # print("Finish searching.")
    return file_list_out

#返回指定目录的所有文件（包含子目录的文件）
def get_all_file(floder_path):
    file_list = []
    if floder_path is None:
        raise Exception("floder_path is None")
    for dirpath, dirnames, filenames in os.walk(floder_path):
        for name in filenames:
            # print(name)
            file_list.append(dirpath + '\\' + name)
    return file_list


#返回指定目录的所有文件夹
def get_all_folder(floder_path):
    file_list = []
    if floder_path is None:
        raise Exception("floder_path is None")
    for dirpath, dirnames, filenames in os.walk(floder_path):
            file_list.append(dirpath)
    return file_list



###统计某个文件的行数
def line_count(file):
    count=0
    num_lines = sum(1 for line in open(file))
    return num_lines
    pass


#主函数，输入文件路径，返回统计行数
def main(file_path="G:\github"):
    file_list = get_all_file(file_path)
    t = is_file_endwith(file_list, ".py")
    count = 0
    for i in t:
        line_num = line_count(i)
        count = count+line_num

    return count


#搜索文件测试
def test_search_file():
    path = "G:\github"
    file_list = get_all_file(path)
    t=is_file_endwith(file_list, ".py")
    print(len(t))

#统计行数测试
def test_linecount():
    file="G:\github\com.zc\cron_test.py"
    t=line_count(file)
    print t

def test_getall_folder():
    path1="G:\github"
    t=get_all_folder(path1)
    print(t)
    return t
    pass


#列出每个文件夹详情
def test_main():
    # test_linecount()
    path="G:/github"
    path1="F:/server_code"
    path2="G:/github\com.zc\spider_zhihu"
    path3="G:/github/com.zc/flight_price"
    path4="G:/github/com.zc/else/old/data_center_update"
    path5="G:/code"
    path6="C:\Users\Administrator\Desktop\FlightStats"
    path7 = "C:\Python27\Lib\site-packages\django"

    # t=main(path4)

    folder=get_all_folder(path7)

    # print(len(folder),folder)
    for i in folder:
        # print(i)
        t=main(i)
        if t == 0:
            continue
        else:
            print(i, "code number is:", t)
    # print(t)
    pass

if __name__ == "__main__":
    # t = main()
    # print t
    test_main()