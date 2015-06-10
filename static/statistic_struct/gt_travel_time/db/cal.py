__author__ = 'Administrator'

import collections



def getData():
    file_in = open("data/last.data")

    G_time_list = []
    D_time_list = []
    Normal_time_list = []

    for line in file_in:
        strArr = line.strip().split("\t")
        if len(strArr) < 6:
            # print(len(strArr))
            continue
        uid = strArr[0]
        train = strArr[1]

        try:
            price = float(strArr[3])
        except Exception as e:
            price = 0

        train_code = train[0]

        if train_code == "G":
            train_type = 1
        elif train_code == "D" or train_code == "C":
            train_type = 2
        else:
            train_type = 3

        departtime = strArr[4]
        arrtime = strArr[5]

        if (len(departtime) != 5) or (len(arrtime) != 5):
            # print(departtime, arrtime)
            continue

        depart_h = int(departtime[0:2])
        depart_m = int(departtime[3:5])
        depart_minute = depart_h*60 + depart_m

        arrive_h = int(arrtime[0:2])
        arrive_m = int(arrtime[3:5])
        arrive_minute = arrive_h*60 + arrive_m

        if arrive_minute < depart_minute:
            arrive_minute += 1440
            diff_minute = arrive_minute - depart_minute

        else:
            diff_minute = arrive_minute - depart_minute

        #
        #
        if diff_minute < 30 and train_type == 3 and price > 100:
            arrive_minute += 1440
            diff_minute = arrive_minute - depart_minute

        if diff_minute < 5 and train_type == 3:
            print(train, price, diff_minute, departtime, arrtime)

        if train_type == 1:
            G_time_list.append(diff_minute)
        elif train_type == 2:
            D_time_list.append(diff_minute)
        else:
            Normal_time_list.append(diff_minute)

        if diff_minute > 1500:
            print(train,price, diff_minute, departtime, depart_minute, arrtime, arrive_minute)

    return G_time_list, D_time_list, Normal_time_list
    # print(len(G_time_list), len(D_time_list), len(Normal_time_list))


def count(time_list, out_file_path):

    out_file = open(out_file_path, "a")
    counter = collections.Counter(time_list)
    for key, value in counter.items():
        out_file.write(str(key) + "\t" + str(value) + "\n")
        pass
    pass

if __name__ == "__main__":
    # getData()
    G_time_list, D_time_list, Normal_time_list = getData()
    count(G_time_list, "data/G_month04.data")
    count(D_time_list, "data/D_month04.data")
    count(Normal_time_list, "data/Normal_month04.data")