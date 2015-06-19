__author__ = 'Administrator'

from os import walk
import xlwt


# excel_out = "lcs_result.xls"
# sheet_name="sheet1"
def lcd():
    lcd_path = "data/lcd/"
    file_list = []
    for root,dirs,files in walk(lcd_path):
        for file_name in files:
            file_list.append(root+file_name)
            print(root+file_name)
    print(file_list)


def excel_write(file_path, name, excel_i=1):
    # fr_in = open(file_path)
    wbk = xlwt.Workbook(encoding='utf-8')
    sheet = wbk.add_sheet(sheet_name)


    fr_in = open(file_path)
    sheet.write(excel_i, 0, name)
    excel_i += 1
    for line in fr_in:
        stringArr = line.strip().split("\t")
        for j, str in enumerate(stringArr):
            sheet.write(excel_i, int(j), str)
        excel_i += 1
    excel_i += 3

    export = excel_out
    wbk.save(export)
    return excel_i

def lcd_main():

    excel_out = "lcs_result.xls"
    sheet_name = "sheet1"
    excel_i = 0

    lcd_path = "data/lcd/"
    wbk = xlwt.Workbook(encoding='utf-8')
    sheet = wbk.add_sheet(sheet_name)

    for root, dirs, files in walk(lcd_path):
        for file_name in files:
            file_path = root+file_name
            fr_in = open(file_path)
            channel = file_name.split("_")[0]
            print(channel)

            sheet.write(excel_i, 0, channel)
            excel_i += 1
            for line in fr_in:
                stringArr = line.strip().split("\t")
                for j, str in enumerate(stringArr):
                    try:
                        str = int(str)
                    except Exception as e:
                        str = str
                    sheet.write(excel_i, int(j), str)
                excel_i += 1
            excel_i += 3

    export = excel_out
    wbk.save(export)



def lcd_main_new():

    excel_out = "lcs_result.xls"
    sheet_name="sheet1"
    excel_i = 0

    lcd_path = "data/lcd/"
    wbk = xlwt.Workbook(encoding='utf-8')
    sheet = wbk.add_sheet(sheet_name)

    for root, dirs, files in walk(lcd_path):
        for file_name in files:
            file_path = root+file_name
            fr_in = open(file_path)
            channel = file_name.strip("_")[0]
            print(channel)

            sheet.write(excel_i, 0, channel)
            excel_i += 1


            for line in fr_in:
                stringArr = line.strip().split("\t")
                for j, str in enumerate(stringArr):
                    try:
                        str = int(str)
                    except Exception as e:
                        str = str
                    sheet.write(excel_i, int(j), str)
                excel_i += 1
            excel_i += 3

    export = excel_out
    wbk.save(export)
lcd_main()