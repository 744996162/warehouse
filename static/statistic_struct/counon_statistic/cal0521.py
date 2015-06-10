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


def coupon_cal(file_in, type):
    """
    gt : type = 1
    hb: type = 2
    channel : type = 3

    """
    coupon_in = open(file_in)
    phoneid_list = []
    for i in coupon_in:
        strArr=i.strip().split("\t")
        phoneid = strArr[0]
        try:
            coupon_type = int(strArr[2])
        except Exception as e:
            coupon_type = 0

        if type == 1:
            if coupon_type in (2, 8, 31):
                phoneid_list.append(phoneid)
        elif type ==2:
            if coupon_type in (12,20,21,22,28,29,30,32,35):
                phoneid_list.append(phoneid)
        elif type == 3 :
            if coupon_type in  (4,5,6,9,10,14,15,16,17,18,19,23,25,36,37):
                phoneid_list.append(phoneid)
    return phoneid_list


def coupon_cal_time(file_in, type):
    """
    gt : type = 1
    hb: type = 2
    channel : type = 3

    """
    coupon_in = open(file_in)
    phoneid_list = []
    for i in coupon_in:
        strArr=i.strip().split("\t")
        phoneid = strArr[0]
        try:
            coupon_type = int(strArr[1])
        except Exception as e:
            coupon_type = 0

        if type == 1:
            if coupon_type in (2, 8, 31):
                phoneid_list.append(phoneid)
        elif type ==2:
            if coupon_type in (12,20,21,22,28,29,30,32,35):
                phoneid_list.append(phoneid)
        elif type == 3 :
            if coupon_type in  (4,5,6,9,10,14,15,16,17,18,19,23,25,36,37):
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

def main(type=1):
    coupon_1 = "data0521/20140701"
    coupon_2 = "data0521/20141001"
    coupon_3 = "data0521/20150101"

    newconsumer_1 = "data0518/newconsumer20140701"
    newconsumer_2 = "data0518/newconsumer20141001"
    newconsumer_3 = "data0518/newconsumer20150101"

    coupon1_list = coupon_cal(coupon_1, type)
    newconsumer1_list = newconsumers_cal(newconsumer_1)
    print("2014Q3", len(coupon1_list), len(set(newconsumer1_list)), len(listRepeat2(coupon1_list,newconsumer1_list)))

    coupon2_list = coupon_cal(coupon_2, type)
    newconsumer2_list = newconsumers_cal(newconsumer_2)
    print("2014Q4", len(coupon2_list), len(set(newconsumer2_list)), len(listRepeat2(coupon2_list, newconsumer2_list)))


    coupon3_list = coupon_cal(coupon_3, type)
    newconsumer3_list = newconsumers_cal(newconsumer_3)
    print("2015Q1", len(coupon3_list), len(set(newconsumer3_list)),len(listRepeat2(coupon3_list, newconsumer3_list)))
    pass

def main_monthly(type=1):
    coupon_1 = "data0521_monthly/20141001"
    coupon_2 = "data0521_monthly/20141101"
    coupon_3 = "data0521_monthly/20141201"

    newconsumer_1 = "data0521_monthly/newconsumer20141001"
    newconsumer_2 = "data0521_monthly/newconsumer20141101"
    newconsumer_3 = "data0521_monthly/newconsumer20141201"

    coupon1_list = coupon_cal(coupon_1, type)
    newconsumer1_list = newconsumers_cal(newconsumer_1)
    print("201410", len(coupon1_list), len(set(newconsumer1_list)), len(listRepeat2(coupon1_list,newconsumer1_list)))

    coupon2_list = coupon_cal(coupon_2, type)
    newconsumer2_list = newconsumers_cal(newconsumer_2)
    print("201411", len(coupon2_list), len(set(newconsumer2_list)), len(listRepeat2(coupon2_list, newconsumer2_list)))


    coupon3_list = coupon_cal(coupon_3, type)
    newconsumer3_list = newconsumers_cal(newconsumer_3)
    print("201412", len(coupon3_list), len(set(newconsumer3_list)),len(listRepeat2(coupon3_list, newconsumer3_list)))
    pass


def main_time(type=1):
    coupon_1 = "data0521_time/20140701"
    coupon_2 = "data0521_time/20141001"
    coupon_3 = "data0521_time/20150101"

    newconsumer_1 = "data0518/newconsumer20140701"
    newconsumer_2 = "data0518/newconsumer20141001"
    newconsumer_3 = "data0518/newconsumer20150101"

    coupon1_list = coupon_cal_time(coupon_1, type)
    newconsumer1_list = newconsumers_cal(newconsumer_1)
    print("2014Q3", len(coupon1_list), len(set(newconsumer1_list)), len(listRepeat2(coupon1_list,newconsumer1_list)))

    coupon2_list = coupon_cal_time(coupon_2, type)
    newconsumer2_list = newconsumers_cal(newconsumer_2)
    print("2014Q4", len(coupon2_list), len(set(newconsumer2_list)), len(listRepeat2(coupon2_list, newconsumer2_list)))

    coupon3_list = coupon_cal_time(coupon_3, type)
    newconsumer3_list = newconsumers_cal(newconsumer_3)
    print("2015Q1", len(coupon3_list), len(set(newconsumer3_list)),len(listRepeat2(coupon3_list, newconsumer3_list)))
    pass


def mainTime_monthly(type=1):
    coupon_1 = "data0521_time_monthly/20141001"
    coupon_2 = "data0521_time_monthly/20141101"
    coupon_3 = "data0521_time_monthly/20141201"

    newconsumer_1 = "data0521_monthly/newconsumer20141001"
    newconsumer_2 = "data0521_monthly/newconsumer20141101"
    newconsumer_3 = "data0521_monthly/newconsumer20141201"

    coupon1_list = coupon_cal_time(coupon_1, type)
    newconsumer1_list = newconsumers_cal(newconsumer_1)
    print("201410", len(coupon1_list), len(set(newconsumer1_list)), len(listRepeat2(coupon1_list,newconsumer1_list)))

    coupon2_list = coupon_cal_time(coupon_2, type)
    newconsumer2_list = newconsumers_cal(newconsumer_2)
    print("201411", len(coupon2_list), len(set(newconsumer2_list)), len(listRepeat2(coupon2_list, newconsumer2_list)))


    coupon3_list = coupon_cal_time(coupon_3, type)
    newconsumer3_list = newconsumers_cal(newconsumer_3)
    print("201412", len(coupon3_list), len(set(newconsumer3_list)),len(listRepeat2(coupon3_list, newconsumer3_list)))
    pass

if __name__ == "__main__":
    # coupon_cal()
    # test1()
    # all_main()
    # price_main()
    # main(1)


    # print("gt")
    # main_monthly(1)
    # print("hb")
    # main_monthly(2)
    # print("channel")
    # main_monthly(3)


    main_time(1)
    main_time(2)
    main_time(3)


    # print("gt")
    # mainTime_monthly(1)
    # print("hb")
    # mainTime_monthly(2)
    # print("channel")
    # mainTime_monthly(3)