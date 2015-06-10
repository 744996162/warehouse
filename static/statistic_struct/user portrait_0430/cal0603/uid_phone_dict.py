__author__ = 'Administrator'
import time
def get_dict():
    gt_file_path = "gt.dat"
    hb_file_path = "hb.dat"

    gt_file = open(gt_file_path)
    hb_file = open(hb_file_path)


    hb_dict = dict()
    gt_dict = dict()
    i=0
    for line in hb_file:
        i += 1
        (uid, phone) = line.strip().split("\t")
        hb_dict[uid] = str(phone)
        if i%1000000 == 0:
            print(i, time.ctime())

    for line in gt_file:
        (uid, phone) = line.strip().split("\t")
        gt_dict[uid] = str(phone)

    hb_file.close()
    gt_file.close()
    return hb_dict, gt_dict


if __name__ == "__main__":
    hb_dict, gt_dict = get_dict()
    print(len(hb_dict), len(gt_dict))
    # print(hb_dict[0])
    pass