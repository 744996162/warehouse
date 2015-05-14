#coding=utf-8



#input指定txt所在文件夹
#output指定excel输出路径
input_file='F:/0zcdata/王伟data/数据完整性test'
output_file='F:/0test'
# text_output=input+'/'+'0log.txt'
# output=open(text_output,'w')
def endWith(s,*endstring):
        array = map(s.endswith,endstring)
        if True in array:
                return True
        else:
                return False
#判断文件中是否包含关键字，是则将文件路径打印出来
def is_file_contain_word(file_list, query_word):
    for _file in file_list:
        if query_word in open(_file).read():
            print(_file)
    #print("Finish searching.")

#返回指定目录的所有文件（包含子目录的文件）
def get_all_file(floder_path):
    import os
    file_list = []
    if floder_path is None:
        raise Exception("floder_path is None")
    for dirpath, dirnames, filenames in os.walk(floder_path):
        for name in filenames:
            file_list.append(dirpath + '/' + name)
    return file_list




