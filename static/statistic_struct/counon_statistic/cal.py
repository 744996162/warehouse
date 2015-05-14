__author__ = 'Administrator'
# # Jar
# coupon_in_path = "data/coupon_0101_0201"
# consumers_in_path = "data/consumer_0201_0301"
# newconsumers_in_path = "data/newconsumer_0101_0201"

#Feb
coupon_in_path = "data/coupon_0201_0301"
consumers_in_path = "data/consumer_0301_0401"
newconsumers_in_path = "data/newconsumer_0201_0301"


def listRepeat(list1, list2):
    listrepeat = []
    for i in list1:
        if i in list2:
            listrepeat.append(i)
    return listrepeat

    pass

def listRepeat2(list1, list2):
    listrepeat = list(set(list1) & set(list2))
    return listrepeat

def coupon_cal(coupon_in):
    # coupon_in_path = "data/coupon_0101_0201"
    # coupon_in = open(coupon_in_path)
    coupon_id_list = []
    coupon_price_list = []
    coupon_type_list = []
    for i in coupon_in:
        # print i
        strArr=i.strip().split("\t")
        id = strArr[0]
        price = strArr[1]
        try:
            coupon_type = "" if strArr[2]== None else strArr[2]
        except:
            coupon_type = ""
        # coupon_id_list.append(id)
        coupon_price_list.append(price)
        coupon_type_list.append(coupon_type)
    # print(coupon_id_list)
    coupon_price_set = set(coupon_price_list)
    coupon_type_set = set(coupon_type_list)
    return coupon_price_set,coupon_type_set

def cal1():
    # coupon_in_path = "data/coupon_0101_0201"
    # consumers_in_path = "data/consumer_0201_0301"
    # newconsumers_in_path = "data/newconsumer_0101_0201"

    coupon_in = open(coupon_in_path)
    consumers_in = open(consumers_in_path)
    newconsumers_in = open(newconsumers_in_path)



    consumers_id_list = []
    for i in consumers_in:
        strArr=i.strip().split("\t")
        id = strArr[0]
        consumers_id_list.append(id)

    newconsumers_id_list = []
    for i in newconsumers_in:
        strArr=i.strip().split("\t")
        id = strArr[0]
        newconsumers_id_list.append(id)


    coupon_id_list = []
    for i in coupon_in:
        strArr=i.strip().split("\t")
        id = strArr[0]
        price = strArr[1]
        try:
            coupon_type = "" if strArr[2]== None else strArr[2]
        except:
            coupon_type = ""

        coupon_id_list.append(id)

    return coupon_id_list, consumers_id_list,newconsumers_id_list


def cal_price():
    coupon_in = open(coupon_in_path)
    consumers_in = open(consumers_in_path)
    newconsumers_in = open(newconsumers_in_path)

    consumers_id_list = []
    for i in consumers_in:
        strArr=i.strip().split("\t")
        id = strArr[0]
        consumers_id_list.append(id)

    newconsumers_id_list = []
    for i in newconsumers_in:
        strArr=i.strip().split("\t")
        id = strArr[0]
        newconsumers_id_list.append(id)


    coupon_price_set, coupon_type_list = coupon_cal(coupon_in)

    coupon_price_list = []
    print(coupon_price_set)
    for price_temp in coupon_price_set:
        print(price_temp)
        coupon_id_list = []
        coupon_in = open(coupon_in_path)
        for i in coupon_in:
            strArr=i.strip().split("\t")
            id = strArr[0]
            price = strArr[1]
            # print(price,price_temp)

            if price == price_temp:

                coupon_id_list.append(id)
        coupon_price_list.append(coupon_id_list)

    return coupon_price_list,coupon_price_set,consumers_id_list,newconsumers_id_list


def cal_coupon_type():
    coupon_in = open(coupon_in_path)
    consumers_in = open(consumers_in_path)
    newconsumers_in = open(newconsumers_in_path)

    consumers_id_list = []
    for i in consumers_in:
        strArr=i.strip().split("\t")
        id = strArr[0]
        consumers_id_list.append(id)

    newconsumers_id_list = []
    for i in newconsumers_in:
        strArr=i.strip().split("\t")
        id = strArr[0]
        newconsumers_id_list.append(id)

    coupon_price_set, coupon_type_set = coupon_cal(coupon_in)

    coupon_type_list = []
    print(coupon_type_set)
    for coupon_type_temp in coupon_type_set:
        # print(coupon_type_temp)
        coupon_id_list = []
        coupon_in = open(coupon_in_path)

        for i in coupon_in:
            strArr=i.strip().split("\t")
            id = strArr[0]
            price = strArr[1]
            try:
                coupon_type = "" if strArr[2]== None else strArr[2]
            except:
                coupon_type = ""
            # print(price,price_temp)

            if coupon_type == coupon_type_temp:

                coupon_id_list.append(id)
        coupon_type_list.append(coupon_id_list)

    return coupon_type_list,coupon_type_set,consumers_id_list,newconsumers_id_list

def statis(coupon_id_list, consumers_id_list,newconsumers_id_list):

    # coupon_id_list, consumers_id_list,newconsumers_id_list = cal1()
    print("coupon_id:"+str(len(coupon_id_list)))
    conpon_count = str(len(coupon_id_list))
    conpon_users = str(len(set(coupon_id_list)))
    new_consumers = str(len(newconsumers_id_list))
    next_month_consumers = str(len(consumers_id_list))

    listrepeat_temp = listRepeat2(set(coupon_id_list), set(newconsumers_id_list))
    new_consumers_use_conpon = str(len(listrepeat_temp))
    listrepeat = listRepeat2(listrepeat_temp, set(consumers_id_list))
    lc = str(len(listrepeat))
    str_out = conpon_count + "\t" + conpon_users + "\t" + new_consumers + "\t" + next_month_consumers + "\t" + new_consumers_use_conpon + "\t" + lc
    return str_out

def all_main():
    coupon_id_list, consumers_id_list,newconsumers_id_list = cal1()
    out_str = statis(coupon_id_list,consumers_id_list,newconsumers_id_list)
    print(out_str)
    pass

def price_main(out_file_path="price_statistics_jar"):
    # out_file_path = "price_statistics_jan"
    out_file = open(out_file_path,"a")

    coupon_price_list,coupon_price_set,consumers_id_list, newconsumers_id_list = cal_price()
    print(len(coupon_price_list),len(coupon_price_set))
    for count,coupon_list in enumerate(coupon_price_list):
        price_type = list(coupon_price_set)[count]
        out_str = statis(coupon_list,consumers_id_list,newconsumers_id_list)
        out_str = price_type + "\t" + out_str
        out_file.write(out_str+"\n")
    coupon_id_list, consumers_id_list,newconsumers_id_list = cal1()
    out_str = statis(coupon_id_list,consumers_id_list,newconsumers_id_list)
    out_str = "all" + "\t" + out_str
    out_file.write(out_str+"\n")
    pass

def type_main(out_file_path="type_statistics_feb"):
    # out_file_path = "price_statistics_jan"
    out_file = open(out_file_path, "a")

    coupon_type_list,coupon_type_set,consumers_id_list, newconsumers_id_list = cal_coupon_type()
    print(len(coupon_type_list), len(coupon_type_set))
    for count, coupon_list in enumerate(coupon_type_list):
        coupon_type = list(coupon_type_set)[count]
        out_str = statis(coupon_list,consumers_id_list,newconsumers_id_list)
        out_str = coupon_type + "\t" + out_str
        out_file.write(out_str+"\n")
    coupon_id_list, consumers_id_list,newconsumers_id_list = cal1()
    out_str = statis(coupon_id_list,consumers_id_list,newconsumers_id_list)
    out_str = "all" + "\t" + out_str
    out_file.write(out_str+"\n")
    pass

if __name__ == "__main__":
    # coupon_cal()
    # test1()
    # all_main()
    # price_main()
    type_main()