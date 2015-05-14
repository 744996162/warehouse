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


def main_6fields():
    inpath="data/ticket_orderdetail_all_android.txt"
    outpath="data/price/ticket_result_price2000plus_female.txt"
    text_read_cal_constellation_6fields(static_result_text=outpath)
    pass

if __name__=="__main__":
    # date="0618"
    # t=constellation_code_to_name(birth_date_classic(date))
    # print t
    # text_read_cal_constellation_2fields()
    # text_read_cal_constellation_6fields()
    main_6fields()
    pass