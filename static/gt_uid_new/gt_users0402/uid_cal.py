__author__ = 'Administrator'
from collections import Counter

uid_base_path = "G:/uid/"
dep_base_path = "G:/dep/"
arr_base_path = "G:/arr/"

file_in = "G:/user_order_test"
path_uid_his_0825 = "G:/data/gt_uid/102his.txt"

uid_file08 = open(uid_base_path + "08", "a")
uid_file09 = open(uid_base_path + "09", "a")
uid_file10 = open(uid_base_path + "10", "a")
uid_file11 = open(uid_base_path + "11", "a")
uid_file12 = open(uid_base_path + "12", "a")
uid_file201501 = open(uid_base_path + "1501", "a")

city_dep08 = open(dep_base_path + "08", "a")
city_dep09 = open(dep_base_path + "09", "a")
city_dep10 = open(dep_base_path + "10", "a")
city_dep11 = open(dep_base_path + "11", "a")
city_dep12 = open(dep_base_path + "12", "a")


city_arr08 = open(arr_base_path + "08", "a")
city_arr09 = open(arr_base_path + "09", "a")
city_arr10 = open(arr_base_path + "10", "a")
city_arr11 = open(arr_base_path + "11", "a")
city_arr12 = open(arr_base_path + "12", "a")



def get_uid_his():
    uid_his = open(path_uid_his_0825)
    list_result = []
    for line in uid_his:
        stringArr = line.strip().split("\t")
        list_result.append(stringArr[0])
    return list_result


def get_uid_month_cal():
    uid_his = open(file_in)
    # uid_list_result08 = []
    # uid_list_result09 = []
    # uid_list_result10 = []
    # uid_list_result11 = []
    # uid_list_result12 = []
    #
    # city_dep_list09 = []
    # city_dep_list10 = []
    # city_dep_list11 = []
    # city_dep_list12 = []
    #
    # city_arr_list09 = []
    # city_arr_list10 = []
    # city_arr_list11 = []
    # city_arr_list12 = []


    for line in uid_his:
        try:
            stringArr = line.strip().split("\t")
            uid = stringArr[0]
            order_date = stringArr[3]
            s_day = order_date[0:4]+order_date[5:7]+order_date[8:10]
            i_day = int(s_day)
            i_status = stringArr[4]
            depart_name = stringArr[6]
            arrive_name = stringArr[7]
            ticket_count = stringArr[8]

            if i_status != "3":
                continue

            if i_day < 20140901:
                # uid_list_result08.append(uid)
                uid_file08.write(uid+"\n")
            elif 20140901 <= i_day < 20141001:
                # uid_list_result09.append(uid)
                uid_file09.write(uid+"\n")
                for i in range(int(ticket_count)):
                    # city_dep_list09.append(depart_name)
                    # city_arr_list09.append(arrive_name)
                    city_dep09.write(depart_name + "\n")
                    city_arr09.write(arrive_name + "\n")

            elif 20141001 <= i_day < 20141101:
                # uid_list_result10.append(uid)
                uid_file10.write(uid+"\n")
                for i in range(int(ticket_count)):
                    # city_dep_list10.append(depart_name)
                    # city_arr_list10.append(arrive_name)
                    city_dep10.write(depart_name + "\n")
                    city_arr10.write(arrive_name + "\n")

            elif 20141101 <= i_day < 20141201:
                # uid_list_result11.append(uid)
                uid_file11.write(uid+"\n")
                for i in range(int(ticket_count)):
                    # city_dep_list11.append(depart_name)
                    # city_arr_list11.append(arrive_name)
                    city_dep11.write(depart_name + "\n")
                    city_arr11.write(arrive_name + "\n")

            elif 20141201 <= i_day < 20150101:
                # uid_list_result12.append(uid)
                uid_file12.write(uid+"\n")
                for i in range(int(ticket_count)):
                    # city_dep_list12.append(depart_name)
                    # city_arr_list12.append(arrive_name)

                    city_dep12.write(depart_name + "\n")
                    city_arr12.write(arrive_name + "\n")
            else:
                uid_file201501.write(uid+"\n")
        except Exception as e:
            print e
    pass


if __name__ == "__main__":
    # result = get_uid_his()
    get_uid_month_cal()