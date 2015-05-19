__author__ = 'Administrator'
import pathlib
import os
import xlwt


def get_all_file(floder_path, key_words):

    file_list = []
    name_list = []

    if floder_path is None:

        raise Exception("floder_path is None")

    for dirpath, dirnames, filenames in os.walk(floder_path):
        for name in filenames:
            if key_words in name:
              file_list.append(dirpath + '/' + name)
              name_list.append(name)
    return file_list,name_list

def excel_write(text_in, excel_out, sheet_name="sheet1"):
    fr_in=open(text_in)
    wbk=xlwt.Workbook(encoding='utf-8')
    sheet=wbk.add_sheet(sheet_name)
    for i,line in enumerate(fr_in.readlines()):
        stringArr = line.strip().split("\t")
        for j, str in enumerate(stringArr):
            sheet.write(int(i),int(j), int(str))
        # print i,stringArr
    export = excel_out
    wbk.save(export)
    return excel_out

def to_excel():

    folder_path = "data/set"
    file_list,name_list = get_all_file(folder_path, ".data")

    print(file_list)
    excel_out = "excel_out.xls"
    wbk = xlwt.Workbook(encoding='utf-8')

    for i, file_path in enumerate(file_list):
        file_name = name_list[i]
        file_name_temp = file_name.strip().split("_")


        date = file_name[0:6]
        gender = file_name_temp[-1][:-5]

        out_file_name = date + gender

        print(date, gender)
        print(file_path, file_name)

        fr_in = open(file_path)
        sheet = wbk.add_sheet(out_file_name)

        data_dict = {}
        for i,line in enumerate(fr_in.readlines()):



            stringArr = line.strip().split("\t")
            data_dict[int(stringArr[0])] = int(stringArr[1])

            for j, str in enumerate(stringArr):
                sheet.write(int(i), int(j), int(str))


        # 18-25
        # 25-35
        # 36-45
        # 46-55
        # 56-65
        # 65+

        print(data_dict)

        sum_0_to_17 = 0
        sum_18_to_25 = 0
        sum_36_to_45 = 0
        sum_46_to_55 = 0
        sum_56_to_65 = 0
        sum_65_upper = 0



        # for key, value in data_dict.items():
        #     if key<= 17:
        #         sum_0_to_17 += value
        #     if 18 <=key <= 25:
        #         sum_18_to_25 += value
        #     if 26 <=key <= 35:
        #         sum_36_to_45 += value
        #     if 46 <=key <= 45:
        #         sum_18_to_25 += value
        #     if 56 <=key <= 55:
        #         sum_18_to_25 += value
        #     if  <=key <= 65:
        #         sum_18_to_25 += value
        #     if key > 65:
        #         sum_18_to_25 += value


        sum_18_to_25 = 0
        # sum_36_to_45 = 0
        # sum_46_to_55 = 0
        # sum_56_to_65 = 0
        # sum_65_upper = 0
        #     sum_0_to_18 += value
        #
        #     print(out_file_name, key, value)


    export = excel_out
    wbk.save(export)

if __name__ == "__main__":
    to_excel()
    pass
