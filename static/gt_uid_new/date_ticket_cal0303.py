#ecoding=utf-8
__author__ = 'Administrator'

def birth_date_classic(date_4str):
    #input date_str
    #output Constellation code
    date_4int=int(date_4str)
    if ((date_4int>=1222 and date_4int<=1231) or date_4int<=119):
        return "A1"
    elif (date_4int>=120 and date_4int<=218):
        return "B2"
    elif (date_4int>=219 and date_4int<=320):
        return "C3"
    elif (date_4int>=321 and date_4int<=419):
        return "D4"
    elif (date_4int>=420 and date_4int<=520):
        return "E5"
    elif (date_4int>=521 and date_4int<=621):
        return "F6"
    elif (date_4int>=622 and date_4int<=722):
        return "G7"
    elif (date_4int>=723 and date_4int<=822):
        return "H8"
    elif (date_4int>=823 and date_4int<=922):
        return "I9"
    elif (date_4int>=923 and date_4int<=1023):
        return "J10"
    elif (date_4int>=1024 and date_4int<=1122):
        return "K11"
    elif (date_4int>=1123 and date_4int<=1221):
        return "L12"
    else:
        return "M0"

def constellation_code_to_name(code):
    if (code=="A1"):
        return "摩羯座"
    elif (code=="B2"):
        return "水瓶座"
    elif (code=="C3"):
        return "双鱼座"
    elif (code=="D4"):
        return "白羊座"
    elif (code=="E5"):
        return "金牛座"
    elif (code=="F6"):
        return "双子座"
    elif (code=="G7"):
        return "巨蟹座"
    elif (code=="H8"):
        return "狮子座"
    elif (code=="I9"):
        return "处女座"
    elif (code=="J10"):
        return "天秤座"
    elif (code=="K11"):
        return "天蝎座"
    elif (code=="L12"):
        return "射手座"
    elif (code=="M0"):
        return "wrong"
    else:
        return "error"

def text_read_cal_constellation_8fields(query_result_text="data0303/ticket_orderdetail_all.txt",static_result_text="data0303/static_result_ticketorder_detail_6.txt"):
    temp_A1=temp_B2=temp_C3=temp_D4=temp_E5=temp_F6=0
    temp_G7=temp_H8=temp_I9=temp_J10=temp_K11=temp_L12=temp_M0=0
    temp_error=0
    fr_in=open(query_result_text)
    result_output=open(static_result_text,'a')
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")
        #身份证号
        date_str=stringArr[2]
        #仓位
        data_cabin=stringArr[3]
        #票价
        data_price=float(stringArr[4])
        #折扣
        data_discount=float(stringArr[5])

        #出发城市
        depcode = stringArr[6]

        #到达城市
        arrcode = stringArr[7]

        #剔除掉身份证号不对的
        if  len(date_str)!=18  :
            # temp_error=temp_error+1
            continue

        date_gender=date_str[16]
        date_4_str=date_str[10:14]

        # if data_price<2000.0:
        #     print(data_price)
        #     continue

        # 性别 17位，奇数为男性，偶数为女性
        if (int(date_gender)+2)%2==1:
            print(date_gender)
            continue

        #折扣
        # if  data_discount>0.3   :
        # if  (data_discount<=0.3 or data_discount>0.7)  :
        # if  data_discount<=0.7  :
        #     print(data_discount)
        #     continue

        #仓位
        # if  (data_cabin!="C" and data_cabin!="J"):
        # if  (data_cabin!="Y"):
        # if  (data_cabin!="F"):
        #
        #     print(data_cabin)
        #     continue

        date_code=birth_date_classic(date_4_str)
        if date_code=="A1":temp_A1=temp_A1+1
        elif date_code=="B2":temp_B2=temp_B2+1
        elif date_code=="C3":temp_C3=temp_C3+1
        elif date_code=="D4":temp_D4=temp_D4+1
        elif date_code=="E5":temp_E5=temp_E5+1
        elif date_code=="F6":temp_F6=temp_F6+1
        elif date_code=="G7":temp_G7=temp_G7+1
        elif date_code=="H8":temp_H8=temp_H8+1
        elif date_code=="I9":temp_I9=temp_I9+1
        elif date_code=="J10":temp_J10=temp_J10+1
        elif date_code=="K11":temp_K11=temp_K11+1
        elif date_code=="L12":temp_L12=temp_L12+1
        elif date_code=="M0":temp_M0=temp_M0+1
        else:temp_error=temp_error+1
        print(date_code)

    out_str1="A1"+","+str(constellation_code_to_name("A1"))+","+str(temp_A1)+'\n'
    out_str2="B2"+","+str(constellation_code_to_name("B2"))+","+str(temp_B2)+'\n'
    out_str3="C3"+","+str(constellation_code_to_name("C3"))+","+str(temp_C3)+'\n'
    out_str4="D4"+","+str(constellation_code_to_name("D4"))+","+str(temp_D4)+'\n'
    out_str5="E5"+","+str(constellation_code_to_name("E5"))+","+str(temp_E5)+'\n'
    out_str6="F6"+","+str(constellation_code_to_name("F6"))+","+str(temp_F6)+'\n'
    out_str7="G7"+","+str(constellation_code_to_name("G7"))+","+str(temp_G7)+'\n'
    out_str8="H8"+","+str(constellation_code_to_name("H8"))+","+str(temp_H8)+'\n'
    out_str9="I9"+","+str(constellation_code_to_name("I9"))+","+str(temp_I9)+'\n'
    out_str10="J10"+","+str(constellation_code_to_name("J10"))+","+str(temp_J10)+'\n'
    out_str11="K11"+","+str(constellation_code_to_name("K11"))+","+str(temp_K11)+'\n'
    out_str12="L12"+","+str(constellation_code_to_name("L12"))+","+str(temp_L12)+'\n'
    out_str13="M0"+","+str(constellation_code_to_name("M0"))+","+str(temp_M0)+'\n'
    out_str14="error"+","+str(constellation_code_to_name("error"))+","+str(temp_error)+'\n'

    out_str_temp1=out_str1+out_str2+out_str3+out_str4+out_str5+out_str6
    out_str_temp2=out_str7+out_str8+out_str9+out_str10+out_str11+out_str12
    out_str=out_str_temp1+out_str_temp2

    result_output.write(out_str+'\n')
        # print(new_date,type(new_date),total,ios,android,type(total))

def main_6fields():
    inpath="data/ticket_orderdetail_all_android.txt"
    outpath="data/price/ticket_result_price2000plus_female.txt"
    text_read_cal_constellation_6fields(static_result_text=outpath)
    pass

def main_8fields():
    outpath="data0303/ticket_result_female.txt"
    text_read_cal_constellation_8fields(static_result_text=outpath)
    pass

def text_change_0303(query_result_text="data0303/ticket_orderdetail_all.txt",static_result_text="data0303/static_result_ticketorder_detail.txt"):
    temp_A1=temp_B2=temp_C3=temp_D4=temp_E5=temp_F6=0
    temp_G7=temp_H8=temp_I9=temp_J10=temp_K11=temp_L12=temp_M0=0
    temp_error=0
    fr_in=open(query_result_text)
    result_output=open(static_result_text,'a')
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")
        #身份证号
        date_cardno=stringArr[2]
        #仓位
        data_cabin=stringArr[3]
        #票价
        data_price=float(stringArr[4])
        #折扣
        data_discount=float(stringArr[5])

        #出发城市
        depcode = stringArr[6]

        #到达城市
        arrcode = stringArr[7]

        #剔除掉身份证号不对的
        if  len(date_cardno)!=18  :
            # temp_error=temp_error+1
            continue

        date_gender=date_cardno[16]
        date_4_str=date_cardno[10:14]

        # 性别 17位，奇数为男性，偶数为女性
        if (int(date_gender)+2)%2==0:
            print(date_gender)
            continue

        #仓位
        # if  (data_cabin!="C" and data_cabin!="J"):
        # if  (data_cabin!="Y"):
        # if  (data_cabin!="F"):
        #
        #     print(data_cabin)
        #     continue
        out_str = date_cardno + "\t" + data_cabin + "\t" + str(data_price)+ "\t" + depcode + "\t" +arrcode
        result_output.write(out_str+'\n')

def average_ticketnum(text_in="data0303/ticket_result_female.txt"):
    fr_in=open(text_in)
    cardno_list=[]
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")
        cardno = stringArr[0]
        cardno_list.append(cardno)

    num_1 = len(cardno_list)
    list_out = list(set(cardno_list))
    num_2 = len(list_out)
    print(num_1,num_2)

    pass


    pass


def getCabinFC(text_in="data0303/ticket_result_female.txt",text_out="data0303/cabin/ticket_result_female.txt"):
    fr_in=open(text_in)
    result_output=open(text_out,'a')
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")
        cardno = stringArr[0]
        data_cabin = stringArr[1]
        # if  (data_cabin!="C" and data_cabin!="J"):
        # if  (data_cabin!="Y"):
        if  (data_cabin!="F"):
        #
            print(data_cabin)
            continue
        else:
            result_output.write(line)
    pass

def cabinF_cal(text_in="data0303/cabin/cabin_female.txt",text_out="data0303/cabin/xingzuo_female_statoc.txt"):
    temp_A1=temp_B2=temp_C3=temp_D4=temp_E5=temp_F6=0
    temp_G7=temp_H8=temp_I9=temp_J10=temp_K11=temp_L12=temp_M0=0
    temp_error=0
    fr_in=open(text_in)
    result_output=open(text_out,'a')
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")

        card_no = stringArr[0]
        date_4_str=card_no[10:14]
        date_code=birth_date_classic(date_4_str)
        if date_code=="A1":temp_A1=temp_A1+1
        elif date_code=="B2":temp_B2=temp_B2+1
        elif date_code=="C3":temp_C3=temp_C3+1
        elif date_code=="D4":temp_D4=temp_D4+1
        elif date_code=="E5":temp_E5=temp_E5+1
        elif date_code=="F6":temp_F6=temp_F6+1
        elif date_code=="G7":temp_G7=temp_G7+1
        elif date_code=="H8":temp_H8=temp_H8+1
        elif date_code=="I9":temp_I9=temp_I9+1
        elif date_code=="J10":temp_J10=temp_J10+1
        elif date_code=="K11":temp_K11=temp_K11+1
        elif date_code=="L12":temp_L12=temp_L12+1
        elif date_code=="M0":temp_M0=temp_M0+1
        else:temp_error=temp_error+1
        print(date_code)

    out_str1="A1"+","+str(constellation_code_to_name("A1"))+","+str(temp_A1)+'\n'
    out_str2="B2"+","+str(constellation_code_to_name("B2"))+","+str(temp_B2)+'\n'
    out_str3="C3"+","+str(constellation_code_to_name("C3"))+","+str(temp_C3)+'\n'
    out_str4="D4"+","+str(constellation_code_to_name("D4"))+","+str(temp_D4)+'\n'
    out_str5="E5"+","+str(constellation_code_to_name("E5"))+","+str(temp_E5)+'\n'
    out_str6="F6"+","+str(constellation_code_to_name("F6"))+","+str(temp_F6)+'\n'
    out_str7="G7"+","+str(constellation_code_to_name("G7"))+","+str(temp_G7)+'\n'
    out_str8="H8"+","+str(constellation_code_to_name("H8"))+","+str(temp_H8)+'\n'
    out_str9="I9"+","+str(constellation_code_to_name("I9"))+","+str(temp_I9)+'\n'
    out_str10="J10"+","+str(constellation_code_to_name("J10"))+","+str(temp_J10)+'\n'
    out_str11="K11"+","+str(constellation_code_to_name("K11"))+","+str(temp_K11)+'\n'
    out_str12="L12"+","+str(constellation_code_to_name("L12"))+","+str(temp_L12)+'\n'
    out_str13="M0"+","+str(constellation_code_to_name("M0"))+","+str(temp_M0)+'\n'
    out_str14="error"+","+str(constellation_code_to_name("error"))+","+str(temp_error)+'\n'

    out_str_temp1=out_str1+out_str2+out_str3+out_str4+out_str5+out_str6
    out_str_temp2=out_str7+out_str8+out_str9+out_str10+out_str11+out_str12+out_str13+out_str14
    out_str=out_str_temp1+out_str_temp2

    result_output.write(out_str+'\n')


def cabinF_age_cal(text_in="data0303/cabin/cabin_female.txt",text_out="data0303/age/age_female_static.txt"):
    # 25以下， 25-35， 35-45， 45-55， 55以上
    temp_25down=temp_25=temp_35=temp_45=temp_55up=0
    fr_in=open(text_in)
    result_output=open(text_out,'a')
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")

        card_no = stringArr[0]
        i_date_year=int(card_no[6:10])
        print(i_date_year)
        if (2015-i_date_year)<25:
            temp_25down += 1
        elif ((2015 - i_date_year) >= 25 and (2015 - i_date_year) < 35) :
            temp_25 += 1
        elif ((2015 - i_date_year) >= 35 and (2015 - i_date_year) < 45) :
            temp_35 += 1
        elif ((2015 - i_date_year) >= 45 and (2015 - i_date_year) < 55) :
            temp_45 += 1
        elif (2015 - i_date_year) >= 55  :
            temp_55up += 1

    out_str1="25岁以下"+"\t"+str(temp_25down)+'\n'
    out_str2="25岁到35岁"+"\t"+str(temp_25)+'\n'
    out_str3="35岁到45岁"+"\t"+str(temp_35)+'\n'
    out_str4="45岁到55岁"+"\t"+str(temp_45)+'\n'
    out_str5="55岁以上"+"\t"+str(temp_55up)+'\n'

    out_str=out_str1+out_str2+out_str3+out_str4+out_str5
    result_output.write(out_str+'\n')

        # date_code=birth_date_classic(date_4_str)
    pass

def city_cal(text_in="data0303/ticket_result_female.txt",text_out="data0303/city/city_female_static.txt"):
    fr_in=open(text_in)
    result_output=open(text_out,'a')
    arrcode_city_list= []
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")

        arrcode_city = stringArr[4]

        arrcode_city_list.append(arrcode_city)


    myset = set(arrcode_city_list)

    for item in myset:
        string_out = item + "\t" +  str(arrcode_city_list.count(item))
        result_output.write(string_out+"\n")
      # print("the %s has found %d" % (item,arrcode_city_list.count(item)))

    pass


def test(text_in="G:/data/102user_sub_order/test.txt",text_out="G:/data/102user_sub_order/result/result.txt"):
    fr_in=open(text_in,encoding= 'utf-8')
    result_output=open(text_out,'a')
    arrcode_city_list_male= []
    arrcode_city_list_female= []

    uid_list = []
    uid_list_female = []
    uid_list_male = []

    count = 0
    count_idcard = 0
    count_GD = 0

    count_female = 0
    count_male = 0

    count_female_gt = 0
    count_male_gt = 0

    count_female_gt_level1 = 0
    count_male_gt_level1 = 0


    city_gt_male_list = []
    city_gt_female_list = []


    male_A1=male_B2=male_C3=male_D4=male_E5=male_F6=0
    male_G7=male_H8=male_I9=male_J10=male_K11=male_L12=male_M0=male_error=0

    female_A1=female_B2=female_C3=female_D4=female_E5=female_F6=0
    female_G7=female_H8=female_I9=female_J10=female_K11=female_L12=female_M0=female_error=0

    male_level1_A1=male_level1_B2=male_level1_C3=male_level1_D4=male_level1_E5=male_level1_F6=0
    male_level1_G7=male_level1_H8=male_level1_I9=male_level1_J10=male_level1_K11=male_level1_L12=male_level1_M0=male_level1_error=0

    female_level1_A1=female_level1_B2=female_level1_C3=female_level1_D4=female_level1_E5=female_level1_F6=0
    female_level1_G7=female_level1_H8=female_level1_I9=female_level1_J10=female_level1_K11=female_level1_L12=female_level1_M0=female_level1_error=0


    # 25以下， 25-35， 35-45， 45-55， 55以上
    male_25down=male_25=male_35=male_45=male_55up=0
    female_25down=female_25=female_35=female_45=female_55up=0

    male_level1_25down=male_level1_25=male_level1_35=male_level1_45=male_level1_55up=0
    female_level1_25down=female_level1_25=female_level1_35=female_level1_45=female_level1_55up=0

    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")
        count += 1
        uid = stringArr[0]
        train_no = stringArr[1]
        depart_name = stringArr[2]
        arrive_name = stringArr[3]
        card_type = stringArr[4]
        card_no = stringArr[5]
        seat_name = stringArr[6]
        status = stringArr[7]
        s_day = stringArr[8]


        train_level = train_no[0]



        if  len(card_no)!=18  :
            continue

        #获取日期
        s_date_4=card_no[10:14]
        date_code=birth_date_classic(s_date_4)

        i_date_year=int(card_no[6:10])

        count_idcard += 1


        date_gender = card_no[16]

        # 性别 17位，奇数为男性，偶数为女性
        if (int(date_gender)+2)%2==1:
            #男性
            count_male += 1
            #若是高铁或动车
            if (train_level=="G" or train_level=="D"):
                uid_list.append(uid)
                uid_list_male.append(uid)
                count_GD += 1
                count_male_gt +=1

                city_gt_male_list.append(arrive_name)

                if date_code=="A1":male_A1=male_A1+1
                elif date_code=="B2":male_B2=male_B2+1
                elif date_code=="C3":male_C3=male_C3+1
                elif date_code=="D4":male_D4=male_D4+1
                elif date_code=="E5":male_E5=male_E5+1
                elif date_code=="F6":male_F6=male_F6+1
                elif date_code=="G7":male_G7=male_G7+1
                elif date_code=="H8":male_H8=male_H8+1
                elif date_code=="I9":male_I9=male_I9+1
                elif date_code=="J10":male_J10=male_J10+1
                elif date_code=="K11":male_K11=male_K11+1
                elif date_code=="L12":male_L12=male_L12+1
                elif date_code=="M0":male_M0=male_M0+1
                else:male_error=male_error+1

                if (2015-i_date_year)<25:
                    male_25down += 1
                elif ((2015 - i_date_year) >= 25 and (2015 - i_date_year) < 35) :
                    male_25 += 1
                elif ((2015 - i_date_year) >= 35 and (2015 - i_date_year) < 45) :
                    male_35 += 1
                elif ((2015 - i_date_year) >= 45 and (2015 - i_date_year) < 55) :
                    male_45 += 1
                elif (2015 - i_date_year) >= 55  :
                    male_55up += 1

                if ("一等座" in seat_name):
                    count_male_gt_level1 += 1
                    if date_code=="A1":male_level1_A1=male_level1_A1+1
                    elif date_code=="B2":male_level1_B2=male_level1_B2+1
                    elif date_code=="C3":male_level1_C3=male_level1_C3+1
                    elif date_code=="D4":male_level1_D4=male_level1_D4+1
                    elif date_code=="E5":male_level1_E5=male_level1_E5+1
                    elif date_code=="F6":male_level1_F6=male_level1_F6+1
                    elif date_code=="G7":male_level1_G7=male_level1_G7+1
                    elif date_code=="H8":male_level1_H8=male_level1_H8+1
                    elif date_code=="I9":male_level1_I9=male_level1_I9+1
                    elif date_code=="J10":male_level1_J10=male_level1_J10+1
                    elif date_code=="K11":male_level1_K11=male_level1_K11+1
                    elif date_code=="L12":male_level1_L12=male_level1_L12+1
                    elif date_code=="M0":male_level1_M0=male_level1_M0+1
                    else:male_level1_error=male_level1_error+1

                    if (2015-i_date_year)<25:
                        male_level1_25down += 1
                    elif ((2015 - i_date_year) >= 25 and (2015 - i_date_year) < 35) :
                        male_level1_25 += 1
                    elif ((2015 - i_date_year) >= 35 and (2015 - i_date_year) < 45) :
                        male_level1_35 += 1
                    elif ((2015 - i_date_year) >= 45 and (2015 - i_date_year) < 55) :
                        male_level1_45 += 1
                    elif (2015 - i_date_year) >= 55  :
                        male_level1_55up += 1
                    pass

        else:
            #女性
            count_female += 1
            #若是高铁或动车
            if (train_level=="G" or train_level=="D"):
                count_GD += 1
                count_female_gt +=1

                uid_list.append(uid)
                uid_list_female.append(uid)


                city_gt_female_list.append(arrive_name)
                if date_code=="A1":female_A1=female_A1+1
                elif date_code=="B2":female_B2=female_B2+1
                elif date_code=="C3":female_C3=female_C3+1
                elif date_code=="D4":female_D4=female_D4+1
                elif date_code=="E5":female_E5=female_E5+1
                elif date_code=="F6":female_F6=female_F6+1
                elif date_code=="G7":female_G7=female_G7+1
                elif date_code=="H8":female_H8=female_H8+1
                elif date_code=="I9":female_I9=female_I9+1
                elif date_code=="J10":female_J10=female_J10+1
                elif date_code=="K11":female_K11=female_K11+1
                elif date_code=="L12":female_L12=female_L12+1
                elif date_code=="M0":female_M0=female_M0+1
                else:female_error=female_error+1

                if (2015-i_date_year)<25:
                    female_25down += 1
                elif ((2015 - i_date_year) >= 25 and (2015 - i_date_year) < 35) :
                    female_25 += 1
                elif ((2015 - i_date_year) >= 35 and (2015 - i_date_year) < 45) :
                    female_35 += 1
                elif ((2015 - i_date_year) >= 45 and (2015 - i_date_year) < 55) :
                    female_45 += 1
                elif (2015 - i_date_year) >= 55  :
                    female_55up += 1

                if ("一等座" in seat_name):
                    count_female_gt_level1 += 1
                    if date_code=="A1":female_level1_A1=female_level1_A1+1
                    elif date_code=="B2":female_level1_B2=female_level1_B2+1
                    elif date_code=="C3":female_level1_C3=female_level1_C3+1
                    elif date_code=="D4":female_level1_D4=female_level1_D4+1
                    elif date_code=="E5":female_level1_E5=female_level1_E5+1
                    elif date_code=="F6":female_level1_F6=female_level1_F6+1
                    elif date_code=="G7":female_level1_G7=female_level1_G7+1
                    elif date_code=="H8":female_level1_H8=female_level1_H8+1
                    elif date_code=="I9":female_level1_I9=female_level1_I9+1
                    elif date_code=="J10":female_level1_J10=female_level1_J10+1
                    elif date_code=="K11":female_level1_K11=female_level1_K11+1
                    elif date_code=="L12":female_level1_L12=female_level1_L12+1
                    elif date_code=="M0":female_level1_M0=female_level1_M0+1
                    else:female_level1_error=female_level1_error+1

                    if (2015-i_date_year)<25:
                        female_level1_25down += 1
                    elif ((2015 - i_date_year) >= 25 and (2015 - i_date_year) < 35) :
                        female_level1_25 += 1
                    elif ((2015 - i_date_year) >= 35 and (2015 - i_date_year) < 45) :
                        female_level1_35 += 1
                    elif ((2015 - i_date_year) >= 45 and (2015 - i_date_year) < 55) :
                        female_level1_45 += 1
                    elif (2015 - i_date_year) >= 55  :
                        female_level1_55up += 1
                    pass


    xingzuo_male_gt1="A1"+","+str(constellation_code_to_name("A1"))+","+str(male_A1)+'\n'
    xingzuo_male_gt2="B2"+","+str(constellation_code_to_name("B2"))+","+str(male_B2)+'\n'
    xingzuo_male_gt3="C3"+","+str(constellation_code_to_name("C3"))+","+str(male_C3)+'\n'
    xingzuo_male_gt4="D4"+","+str(constellation_code_to_name("D4"))+","+str(male_D4)+'\n'
    xingzuo_male_gt5="E5"+","+str(constellation_code_to_name("E5"))+","+str(male_E5)+'\n'
    xingzuo_male_gt6="F6"+","+str(constellation_code_to_name("F6"))+","+str(male_F6)+'\n'
    xingzuo_male_gt7="G7"+","+str(constellation_code_to_name("G7"))+","+str(male_G7)+'\n'
    xingzuo_male_gt8="H8"+","+str(constellation_code_to_name("H8"))+","+str(male_H8)+'\n'
    xingzuo_male_gt9="I9"+","+str(constellation_code_to_name("I9"))+","+str(male_I9)+'\n'
    xingzuo_male_gt10="J10"+","+str(constellation_code_to_name("J10"))+","+str(male_J10)+'\n'
    xingzuo_male_gt11="K11"+","+str(constellation_code_to_name("K11"))+","+str(male_K11)+'\n'
    xingzuo_male_gt12="L12"+","+str(constellation_code_to_name("L12"))+","+str(male_L12)+'\n'
    xingzuo_male_gt13="M0"+","+str(constellation_code_to_name("M0"))+","+str(male_M0)+'\n'
    xingzuo_male_gt14="error"+","+str(constellation_code_to_name("error"))+","+str(male_error)+'\n'

    xingzuo_male_gt_temp1=xingzuo_male_gt1+xingzuo_male_gt2+xingzuo_male_gt3+xingzuo_male_gt4+xingzuo_male_gt5+xingzuo_male_gt6
    xingzuo_male_gt_temp2=xingzuo_male_gt7+xingzuo_male_gt8+xingzuo_male_gt9+xingzuo_male_gt10+xingzuo_male_gt11+xingzuo_male_gt12+xingzuo_male_gt13+xingzuo_male_gt14
    xingzuo_male_gt=xingzuo_male_gt_temp1+xingzuo_male_gt_temp2

    xingzuo_male_level1_gt1="A1"+","+str(constellation_code_to_name("A1"))+","+str(male_level1_A1)+'\n'
    xingzuo_male_level1_gt2="B2"+","+str(constellation_code_to_name("B2"))+","+str(male_level1_B2)+'\n'
    xingzuo_male_level1_gt3="C3"+","+str(constellation_code_to_name("C3"))+","+str(male_level1_C3)+'\n'
    xingzuo_male_level1_gt4="D4"+","+str(constellation_code_to_name("D4"))+","+str(male_level1_D4)+'\n'
    xingzuo_male_level1_gt5="E5"+","+str(constellation_code_to_name("E5"))+","+str(male_level1_E5)+'\n'
    xingzuo_male_level1_gt6="F6"+","+str(constellation_code_to_name("F6"))+","+str(male_level1_F6)+'\n'
    xingzuo_male_level1_gt7="G7"+","+str(constellation_code_to_name("G7"))+","+str(male_level1_G7)+'\n'
    xingzuo_male_level1_gt8="H8"+","+str(constellation_code_to_name("H8"))+","+str(male_level1_H8)+'\n'
    xingzuo_male_level1_gt9="I9"+","+str(constellation_code_to_name("I9"))+","+str(male_level1_I9)+'\n'
    xingzuo_male_level1_gt10="J10"+","+str(constellation_code_to_name("J10"))+","+str(male_level1_J10)+'\n'
    xingzuo_male_level1_gt11="K11"+","+str(constellation_code_to_name("K11"))+","+str(male_level1_K11)+'\n'
    xingzuo_male_level1_gt12="L12"+","+str(constellation_code_to_name("L12"))+","+str(male_level1_L12)+'\n'
    xingzuo_male_level1_gt13="M0"+","+str(constellation_code_to_name("M0"))+","+str(male_level1_M0)+'\n'
    xingzuo_male_level1_gt14="error"+","+str(constellation_code_to_name("error"))+","+str(male_level1_error)+'\n'

    xingzuo_male_level1_gt_temp1=xingzuo_male_level1_gt1+xingzuo_male_level1_gt2+xingzuo_male_level1_gt3+xingzuo_male_level1_gt4+xingzuo_male_level1_gt5+xingzuo_male_level1_gt6
    xingzuo_male_level1_gt_temp2=xingzuo_male_level1_gt7+xingzuo_male_level1_gt8+xingzuo_male_level1_gt9+xingzuo_male_level1_gt10+xingzuo_male_level1_gt11+xingzuo_male_level1_gt12+xingzuo_male_level1_gt13+xingzuo_male_level1_gt14
    xingzuo_male_level1_gt=xingzuo_male_level1_gt_temp1+xingzuo_male_level1_gt_temp2

    
    xingzuo_female_gt1="A1"+","+str(constellation_code_to_name("A1"))+","+str(female_A1)+'\n'
    xingzuo_female_gt2="B2"+","+str(constellation_code_to_name("B2"))+","+str(female_B2)+'\n'
    xingzuo_female_gt3="C3"+","+str(constellation_code_to_name("C3"))+","+str(female_C3)+'\n'
    xingzuo_female_gt4="D4"+","+str(constellation_code_to_name("D4"))+","+str(female_D4)+'\n'
    xingzuo_female_gt5="E5"+","+str(constellation_code_to_name("E5"))+","+str(female_E5)+'\n'
    xingzuo_female_gt6="F6"+","+str(constellation_code_to_name("F6"))+","+str(female_F6)+'\n'
    xingzuo_female_gt7="G7"+","+str(constellation_code_to_name("G7"))+","+str(female_G7)+'\n'
    xingzuo_female_gt8="H8"+","+str(constellation_code_to_name("H8"))+","+str(female_H8)+'\n'
    xingzuo_female_gt9="I9"+","+str(constellation_code_to_name("I9"))+","+str(female_I9)+'\n'
    xingzuo_female_gt10="J10"+","+str(constellation_code_to_name("J10"))+","+str(female_J10)+'\n'
    xingzuo_female_gt11="K11"+","+str(constellation_code_to_name("K11"))+","+str(female_K11)+'\n'
    xingzuo_female_gt12="L12"+","+str(constellation_code_to_name("L12"))+","+str(female_L12)+'\n'
    xingzuo_female_gt13="M0"+","+str(constellation_code_to_name("M0"))+","+str(female_M0)+'\n'
    xingzuo_female_gt14="error"+","+str(constellation_code_to_name("error"))+","+str(female_error)+'\n'

    xingzuo_female_gt_temp1=xingzuo_female_gt1+xingzuo_female_gt2+xingzuo_female_gt3+xingzuo_female_gt4+xingzuo_female_gt5+xingzuo_female_gt6
    xingzuo_female_gt_temp2=xingzuo_female_gt7+xingzuo_female_gt8+xingzuo_female_gt9+xingzuo_female_gt10+xingzuo_female_gt11+xingzuo_female_gt12+xingzuo_female_gt13+xingzuo_female_gt14
    xingzuo_female_gt=xingzuo_female_gt_temp1+xingzuo_female_gt_temp2



    xingzuo_female_level1_gt1="A1"+","+str(constellation_code_to_name("A1"))+","+str(female_level1_A1)+'\n'
    xingzuo_female_level1_gt2="B2"+","+str(constellation_code_to_name("B2"))+","+str(female_level1_B2)+'\n'
    xingzuo_female_level1_gt3="C3"+","+str(constellation_code_to_name("C3"))+","+str(female_level1_C3)+'\n'
    xingzuo_female_level1_gt4="D4"+","+str(constellation_code_to_name("D4"))+","+str(female_level1_D4)+'\n'
    xingzuo_female_level1_gt5="E5"+","+str(constellation_code_to_name("E5"))+","+str(female_level1_E5)+'\n'
    xingzuo_female_level1_gt6="F6"+","+str(constellation_code_to_name("F6"))+","+str(female_level1_F6)+'\n'
    xingzuo_female_level1_gt7="G7"+","+str(constellation_code_to_name("G7"))+","+str(female_level1_G7)+'\n'
    xingzuo_female_level1_gt8="H8"+","+str(constellation_code_to_name("H8"))+","+str(female_level1_H8)+'\n'
    xingzuo_female_level1_gt9="I9"+","+str(constellation_code_to_name("I9"))+","+str(female_level1_I9)+'\n'
    xingzuo_female_level1_gt10="J10"+","+str(constellation_code_to_name("J10"))+","+str(female_level1_J10)+'\n'
    xingzuo_female_level1_gt11="K11"+","+str(constellation_code_to_name("K11"))+","+str(female_level1_K11)+'\n'
    xingzuo_female_level1_gt12="L12"+","+str(constellation_code_to_name("L12"))+","+str(female_level1_L12)+'\n'
    xingzuo_female_level1_gt13="M0"+","+str(constellation_code_to_name("M0"))+","+str(female_level1_M0)+'\n'
    xingzuo_female_level1_gt14="error"+","+str(constellation_code_to_name("error"))+","+str(female_level1_error)+'\n'

    xingzuo_female_level1_gt_temp1=xingzuo_female_level1_gt1+xingzuo_female_level1_gt2+xingzuo_female_level1_gt3+xingzuo_female_level1_gt4+xingzuo_female_level1_gt5+xingzuo_female_level1_gt6
    xingzuo_female_level1_gt_temp2=xingzuo_female_level1_gt7+xingzuo_female_level1_gt8+xingzuo_female_level1_gt9+xingzuo_female_level1_gt10+xingzuo_female_level1_gt11+xingzuo_female_level1_gt12+xingzuo_female_level1_gt13+xingzuo_female_level1_gt14
    xingzuo_female_level1_gt=xingzuo_female_level1_gt_temp1+xingzuo_female_level1_gt_temp2

    result_output.write("高铁乘客统计:"+"\n")
    result_output.write("乘客数量:"+","+str(count)+"\n")
    result_output.write("有效身份证件数量:"+","+str(count_idcard)+"\n")
    result_output.write("男性乘客数量:"+","+str(count_male)+"\n")
    result_output.write("女性乘客数量:"+","+str(count_female)+"\n")
    result_output.write("高铁乘客数量:"+","+str(count_GD)+"\n")
    result_output.write("男性高铁乘客数量:"+","+str(count_male_gt)+"\n")
    result_output.write("女性高铁乘客数量:"+","+str(count_female_gt)+"\n")
    result_output.write("男性一等座乘客数量:"+","+str(count_male_gt_level1)+"\n")
    result_output.write("女性一等座乘客数量:"+","+str(count_female_gt_level1)+"\n")



    result_output.write("高铁星座统计:"+"\n")
    result_output.write("男性高铁星座统计:"+"\n")
    result_output.write(xingzuo_male_gt+"\n")

    result_output.write("男性高铁一等座星座统计:"+"\n")
    result_output.write(xingzuo_male_level1_gt+"\n")

    result_output.write("女性高铁星座统计:"+"\n")
    result_output.write(xingzuo_female_gt+"\n")

    result_output.write("女性高铁一等座星座统计:"+"\n")
    result_output.write(xingzuo_female_level1_gt+"\n")

    uid_list_male_set = set(uid_list_male)
    result_output.write("男性用户去重:"+"\t"+str(len(uid_list_male_set))+"\n")

    uid_list_female_set = set(uid_list_female)
    result_output.write("女性用户去重:"+"\t"+str(len(uid_list_female_set))+"\n")


    result_output.write("男性高铁年龄统计:"+"\n")
    nianling_male_gt1 = "25岁以下"+"\t"+str(male_25down)+'\n'
    nianling_male_gt2 = "25岁到35岁"+"\t"+str(male_25)+'\n'
    nianling_male_gt3 = "35岁到45岁"+"\t"+str(male_35)+'\n'
    nianling_male_gt4 = "45岁到55岁"+"\t"+str(male_45)+'\n'
    nianling_male_gt5 = "55岁以上"+"\t"+str(male_55up)+'\n'

    nianling_male = nianling_male_gt1+nianling_male_gt2+nianling_male_gt3+nianling_male_gt4+nianling_male_gt5


    nianling_male_level1_gt1 = "25岁以下"+"\t"+str(male_level1_25down)+'\n'
    nianling_male_level1_gt2 = "25岁到35岁"+"\t"+str(male_level1_25)+'\n'
    nianling_male_level1_gt3 = "35岁到45岁"+"\t"+str(male_level1_35)+'\n'
    nianling_male_level1_gt4 = "45岁到55岁"+"\t"+str(male_level1_45)+'\n'
    nianling_male_level1_gt5 = "55岁以上"+"\t"+str(male_level1_55up)+'\n'

    nianling_male_level1 = nianling_male_level1_gt1+nianling_male_level1_gt2+nianling_male_level1_gt3+nianling_male_level1_gt4+nianling_male_level1_gt5



    nianling_female_gt1 = "25岁以下"+"\t"+str(female_25down)+'\n'
    nianling_female_gt2 = "25岁到35岁"+"\t"+str(female_25)+'\n'
    nianling_female_gt3 = "35岁到45岁"+"\t"+str(female_35)+'\n'
    nianling_female_gt4 = "45岁到55岁"+"\t"+str(female_45)+'\n'
    nianling_female_gt5 = "55岁以上"+"\t"+str(female_55up)+'\n'

    nianling_female = nianling_female_gt1+nianling_female_gt2+nianling_female_gt3+nianling_female_gt4+nianling_female_gt5


    nianling_female_level1_gt1 = "25岁以下"+"\t"+str(female_level1_25down)+'\n'
    nianling_female_level1_gt2 = "25岁到35岁"+"\t"+str(female_level1_25)+'\n'
    nianling_female_level1_gt3 = "35岁到45岁"+"\t"+str(female_level1_35)+'\n'
    nianling_female_level1_gt4 = "45岁到55岁"+"\t"+str(female_level1_45)+'\n'
    nianling_female_level1_gt5 = "55岁以上"+"\t"+str(female_level1_55up)+'\n'

    nianling_female_level1 = nianling_female_level1_gt1+nianling_female_level1_gt2+nianling_female_level1_gt3+nianling_female_level1_gt4+nianling_female_level1_gt5


    result_output.write("男性高铁年龄统计"+"\n")
    result_output.write(nianling_male+"\n")

    result_output.write("男性高铁一等座年龄统计"+"\n")
    result_output.write(nianling_male_level1+"\n")

    result_output.write("女性高铁年龄统计"+"\n")
    result_output.write(nianling_female+"\n")

    result_output.write("女性高铁一等座年龄统计"+"\n")
    result_output.write(nianling_female_level1+"\n")






    male_city_set = set(city_gt_male_list)
    result_output.write("男性出行城市统计"+"\n")

    for item in male_city_set:
        string_out = item + "\t" +  str(city_gt_male_list.count(item))
        result_output.write(string_out+"\n")

    female_city_set = set(city_gt_female_list)
    result_output.write("女性出行城市统计"+"\n")
    for item in female_city_set:
        string_out = item + "\t" +  str(city_gt_female_list.count(item))
        result_output.write(string_out+"\n")


def test2(text_in="G:/data/102user_sub_order/test.txt",text_out="G:/data/102user_sub_order/result/s_day_static.txt"):
    fr_in = open(text_in,encoding= 'utf-8')
    result_output = open(text_out,'a')
    s_day_list = []
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")
        s_day = stringArr[8]
        s_day_list.append(s_day)
    s_day_list_set = set(s_day_list)

    for item in s_day_list_set:
        string_out = item + "\t" +  str(s_day_list.count(item))
        result_output.write(string_out+"\n")

if __name__=="__main__":
    # date="0618"
    # t=constellation_code_to_name(birth_date_classic(date))
    # print t
    # text_read_cal_constellation_2fields()
    # text_read_cal_constellation_6fields()
    # main_6fields()
    outpath="data0303/ticket_result_male.txt"
    # text_change_0303(static_result_text=outpath)

    male_path_in = "data0303/ticket_result_male.txt"
    female_path_in = "data0303/ticket_result_female.txt"

    male_path_out = "data0303/cabin/cabinF_male.txt"
    female_path_out = "data0303/cabin/cabinF_female.txt"

    # average_ticketnum()

    # getCabinFC(male_path_in,male_path_out)
    # getCabinFC(female_path_in,female_path_out)

    # cabinF_cal("data0303/cabin/cabin_male.txt","data0303/cabin/xingzuo_male_static.txt")
    # cabinF_cal("data0303/cabin/cabin_female.txt","data0303/cabin/xingzuo_female_static.txt")
    # cabinF_age_cal()

    # cabinF_age_cal(text_in="data0303/ticket_result_female.txt",text_out="data0303/age/age_female_static.txt")
    #cabinF_age_cal(text_in="data0303/ticket_result_male.txt",text_out="data0303/age/age_male_static.txt")
    # city_cal("data0303/ticket_result_female.txt","data0303/city/city_female_static.txt")
    # city_cal("data0303/ticket_result_male.txt","data0303/city/city_male_static.txt")

    # test(text_in="G:/data/102user_sub_order/user_sub_order.txt",text_out="G:/data/102user_sub_order/result/result.txt")
    test2(text_in="G:/data/102user_sub_order/user_sub_order.txt")
    pass