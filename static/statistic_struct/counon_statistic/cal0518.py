__author__ = 'Administrator'
# # Jar
# coupon_in_path = "data/coupon_0101_0201"
# consumers_in_path = "data/consumer_0201_0301"
# newconsumers_in_path = "data/newconsumer_0101_0201"




def listRepeat(list1, list2):
    listrepeat = []
    for i in list1:
        if i in list2:
            listrepeat.append(i)
    return listrepeat


def listRepeat2(list1, list2):
    listrepeat = list(set(list1) & set(list2))
    return listrepeat


def coupon_cal(file_in):
    coupon_in = open(file_in)
    phoneid_list = []
    for i in coupon_in:
        strArr=i.strip().split("\t")
        phoneid = strArr[0]
        phoneid_list.append(phoneid)
    return phoneid_list

def newconsumers_cal(file_in):
    coupon_in = open(file_in)
    phoneid_list = []
    for i in coupon_in:
        strArr=i.strip().split("\t")
        phoneid = strArr[0]
        phoneid_list.append(phoneid)
    return phoneid_list

def main():
    coupon_1 = "data0518/20140701"
    coupon_2 = "data0518/20141001"
    coupon_3 = "data0518/20150101"

    newconsumer_1 = "data0518/newconsumer20140701"
    newconsumer_2 = "data0518/newconsumer20141001"
    newconsumer_3 = "data0518/newconsumer20150101"

    coupon1_list = coupon_cal(coupon_1)
    newconsumer1_list = coupon_cal(newconsumer_1)
    print("2014Q3", len(coupon1_list), len(set(newconsumer1_list)), len(listRepeat2(coupon1_list,newconsumer1_list)))

    coupon2_list = coupon_cal(coupon_2)
    newconsumer2_list = coupon_cal(newconsumer_2)
    print("2014Q4", len(coupon2_list), len(set(newconsumer2_list)),len(listRepeat2(coupon2_list, newconsumer2_list)))


    coupon3_list = coupon_cal(coupon_3)
    newconsumer3_list = coupon_cal(newconsumer_3)
    print("2015Q1", len(coupon3_list), len(set(newconsumer3_list)),len(listRepeat2(coupon3_list, newconsumer3_list)))


    pass
if __name__ == "__main__":
    # coupon_cal()
    # test1()
    # all_main()
    # price_main()
    main()