__author__ = 'Administrator'
import time

def get_data():
    gt_file_path = "gt.dat"
    hb_file_path = "hb.dat"

    gt_file = open(gt_file_path)
    hb_file = open(hb_file_path)

    i=0
    hb_phone_list = []
    gt_phone_list = []

    for line in hb_file:
        i += 1
        (uid, phone) = line.strip().split("\t")
        hb_phone_list.append(phone)


    for line in gt_file:
        (uid, phone) = line.strip().split("\t")
        gt_phone_list.append(phone)

    hb_file.close()
    gt_file.close()


    hb_phone_set = set(hb_phone_list)
    gt_phone_set = set(gt_phone_list)
    print("app", "list_num", "set_num", "union_num")
    print("hb", len(hb_phone_list), len(hb_phone_set), len(hb_phone_set & gt_phone_set))
    print("gt", len(gt_phone_list), len(gt_phone_set), len(hb_phone_set & gt_phone_set))


if __name__ == "__main__":
    get_data()