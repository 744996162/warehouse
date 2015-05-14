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

def text_read_cal_constellation_2fields(query_result_text="result1.txt",static_result_text="static_result.txt"):
    temp_A1=temp_B2=temp_C3=temp_D4=temp_E5=temp_F6=0
    temp_G7=temp_H8=temp_I9=temp_J10=temp_K11=temp_L12=temp_M0=0
    temp_error=0
    fr_in=open(query_result_text)
    result_output=open(static_result_text,'a')
    for line in fr_in.readlines():
        stringArr=line.strip().split(",")

        date_str=stringArr[1]
        if  len(date_str)<10:
            date_str="9999-99-99"
        date_4_str=date_str[5:7]+date_str[8:10]
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

def text_read_cal_constellation_6fields(query_result_text="data/ticket_orderdetail_all_6.txt",static_result_text="data/static_result_ticketorder_detail_6.txt"):
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

        #剔除掉身份证号不对的
        if  len(date_str)!=18  :
            # temp_error=temp_error+1
            continue

        date_gender=date_str[16]
        date_4_str=date_str[10:14]

        if data_price<2000.0:
            print(data_price)
            continue

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
    city_cal("data0303/ticket_result_female.txt","data0303/city/city_female_static.txt")
    city_cal("data0303/ticket_result_male.txt","data0303/city/city_male_static.txt")
    pass