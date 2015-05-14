#ecoding=utf-8
__author__ = 'Administrator'
import city_query
import numpy as np

def text_phone_id_cal(text_in="data/checkin_result.txt",text_out="data/checkin_SH.txt"):
    fr_in=open(text_in)
    result_output=open(text_out,'a')
    city_obj=city_query.PhoneUserDao()
    i_phone=0
    i_id=0
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")
        #身份证号
        # d_code=stringArr[5]
        # print(d_code)
        #手机号
        # phone_code=stringArr[3]
        try:
            phone_code=stringArr[3]
            phone_code_query=int(phone_code[0:7])
        except Exception as e:
            phone_code_query=0000000

        try:
            d_code=stringArr[5]
            d_code_query=d_code[0:3]
        except Exception as e:
            d_code_query="000"



        sheng,shi=city_obj.query_city(phone_code_query)
        # print(phone_code_query)

        # if d_code_query=="310" :
        #     print("shanghai","d_code")
        #     i_id=i_id+1
        #
        # if shi=="shanghai":
        #     print("SHANGHAI","phone_code")
        #     i_phone=i_phone+1
        if  (d_code_query=="310" or shi=="shanghai"):
            result_output.write(line)
            i_id=i_id+1
            pass
    print(i_id,i_phone)
    pass


def text_cabin_F(text_in="data/checkin_SH.txt",text_out="data/checkin_cabinF.txt"):
    fr_in=open(text_in)
    result_output=open(text_out,'a')
    i=0
    for line in fr_in.readlines():
        #仓位
        stringArr=line.strip().split("\t")
        #仓位
        try:
            cabin=stringArr[4]
        except Exception as e:
            cabin="Y"

        if (cabin!="A" and cabin!="F" and cabin!="C" and cabin!="D" and cabin!="J"):
            continue
        else:
            result_output.write(line)
            i=i+1
    print(i)



def text_list_set(text_in="data/checkin_cabinF.txt",text_out="listset/checkin_SH_set_cabinF.txt"):
    error="listset/checkin_SH_static_error.txt"
    fr_in=open(text_in)
    result_output=open(text_out,'w')
    error_out=open(error,'w')
    i=0
    list_user_id=[]
    #get distinct phone_id
    for line in fr_in.readlines():

        stringArr=line.strip().split("\t")

        user_id=stringArr[0]
        list_user_id.append(user_id)
        i=i+1
    # print(i)
    list_user_id_set=set(list_user_id)
    print(len(list_user_id_set))
    np_list=np.zeros((len(list_user_id_set),10))
    list_idno=[]
    # get start result array store in np_list
    for i,user_id_temp in enumerate(list_user_id_set):

        try:
            np_list[i,0]=int(user_id_temp)
            list_idno.append("0")
        except Exception as e:
            np_list[i,0]=0
        # print(np_list[i])

    # print("np_list")

    temp_num=0
    fr_in2=open(text_in)
    for line in fr_in2.readlines():
        try:
            stringArr=line.strip().split("\t")

            user_id=stringArr[0]
            cabin=stringArr[4]
            idcardtype=stringArr[6]

            idcardno=stringArr[5]
            phone_number=stringArr[3]

            # print(line)
            temp_num=temp_num+1
            print(temp_num)
            for i,num in enumerate(np_list):
                # print(int(np_list[i][0]),int(phone_id))

                try:
                    if str(int(np_list[i][0]))==user_id:
                        list_idno[i]=idcardno
                        if (cabin=="F" or cabin=="A"):
                            np_list[i][1]=int(np_list[i][1])+1
                        elif (cabin=="C" or cabin=="J" or cabin=="D"):
                            np_list[i][2]=int(np_list[i][2])+1
                        else:
                            np_list[i][3]=int(np_list[i][3])+1

                        if idcardtype=="NI":
                            pass
                        else:
                            np_list[i][4]=int(np_list[i][4])+1


                        if np_list[i][6]==0 and len(phone_number)==11:
                            np_list[i][6]=int(phone_number)


                        if np_list[i][7]==0 and idcardtype=="NI" and len(idcardno)==18:
                            try:
                                np_list[i][8]=2015-int(idcardno[6:10])
                                np_list[i][9]=int(idcardno[16:17])%2
                            except Exception as e:
                                pass

                        list_idno[i]=idcardno
                except Exception as e:
                    error_out.write(line+"\n")
                    print(line)
        except Exception as e:
                continue

    for i,line in enumerate(np_list):
        string_out1=str(int(np_list[i][0]))+"\t"+str(int(np_list[i][1]))+"\t"+str(int(np_list[i][2]))+"\t"+str(int(np_list[i][3]))+"\t"+str(int(np_list[i][4]))+"\t"+str(int(np_list[i][5]))
        string_out2=str(int(np_list[i][6]))+"\t"+list_idno[i]+"\t"+str(int(np_list[i][8]))+"\t"+str(int(np_list[i][9]))
        string_out=string_out1+"\t"+string_out2
        result_output.write(string_out+"\n")

    print(np_list)

if __name__=="__main__":
    # text_phone_id_cal()
    # text_cabin_F()
    text_list_set(text_in="data/checkin_SH.txt",text_out="listset/checkin_SH_result.txt")
    pass