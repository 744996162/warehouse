#ecoding=utf-8
__author__ = 'Administrator'
import city_query
import numpy as np

def text_phone_id_cal(text_in="data/ticket_order_test.txt",text_out="data/ticket_SH.txt"):
    fr_in=open(text_in)
    result_output=open(text_out,'a')
    city_obj=city_query.PhoneUserDao()
    i_phone=0
    i_id=0
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")
        #身份证号
        d_code=stringArr[3]
        #手机号
        phone_code=stringArr[2]
        try:
            phone_code_query=int(phone_code[0:7])
        except Exception as e:
            phone_code_query=0000000

        try:
            d_code_query=d_code[0:3]
        except Exception as e:
            d_code_query="000"

        #证件类型
        d_tye=stringArr[4]
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


def text_cabin_F(text_in="data/ticket_SH.txt",text_out="data/ticket_cabinF.txt"):
    fr_in=open(text_in)
    result_output=open(text_out,'a')
    i=0
    for line in fr_in.readlines():
        #仓位
        stringArr=line.strip().split("\t")
        #仓位
        cabin=stringArr[5]

        if cabin!="Y":
            result_output.write(line)
            i=i+1
    print(i)


def text_list_set(text_in="data/ticket_SH.txt",text_out="listset/ticket_SH_set_new0127.txt"):
    error="listset/ticket_SH_static_error.txt"
    fr_in=open(text_in)
    result_output=open(text_out,'w')
    error_out=open(error,'w')
    i=0
    list_phone_id=[]
    #get distinct phone_id
    for line in fr_in.readlines():

        stringArr=line.strip().split("\t")

        phone_id=stringArr[1]
        list_phone_id.append(phone_id)
        i=i+1
    # print(i)
    list_phone_id_set=set(list_phone_id)
    # print(len(list_phone_id_set))
    np_list=np.zeros((len(list_phone_id_set),6))

    # get start result array store in np_list
    for i,phone_id_temp in enumerate(list_phone_id_set):

        try:
            np_list[i,0]=int(phone_id_temp)
        except Exception as e:
            np_list[i,0]=0
        # print(np_list[i])

    print("np_list")

    #遍历文本
    temp_num=0
    fr_in2=open(text_in)
    for line in fr_in2.readlines():
        stringArr=line.strip().split("\t")
        phone_id=stringArr[1]
        cabin=stringArr[5]
        idcardtype=stringArr[4]
        # print(line)
        temp_num=temp_num+1
        print(temp_num)
        for i,num in enumerate(np_list):
            # print(int(np_list[i][0]),int(phone_id))
            try:
                if str(int(np_list[i][0]))==phone_id:
                    if cabin=="F":
                        np_list[i][1]=int(np_list[i][1])+1
                    elif (cabin=="C" or cabin=="J"):
                        np_list[i][2]=int(np_list[i][2])+1
                    elif cabin=="Y":
                        np_list[i][3]=int(np_list[i][3])+1
                    else:
                        pass

                    if idcardtype=="0":
                        pass
                    else:
                        np_list[i][4]=int(np_list[i][4])+1
            except Exception as e:
                error_out.write(line+"\n")
                print(line)

                # print(int(np_list[i][0]),int(phone_id))
                # temp_num=temp_num+1
        # print(temp_num)
        # if cabin==F
    for i,line in enumerate(np_list):
        string_out=str(int(np_list[i][0]))+"\t"+str(int(np_list[i][1]))+"\t"+str(int(np_list[i][2]))+"\t"+str(int(np_list[i][3]))+"\t"+str(int(np_list[i][4]))
        result_output.write(string_out+"\n")

    print(np_list)


def text_list_set_new0127(text_in="data/ticket_cabinF.txt",text_out="listset/ticket_SH_set_new0127.txt"):
    error="listset/ticket_SH_static_error.txt"
    fr_in=open(text_in)
    result_output=open(text_out,'w')
    error_out=open(error,'w')
    i=0
    list_phone_id=[]
    #get distinct phone_id
    for line in fr_in.readlines():

        stringArr=line.strip().split("\t")

        phone_id=stringArr[1]
        list_phone_id.append(phone_id)
        i=i+1
    # print(i)
    list_phone_id_set=set(list_phone_id)
    # print(len(list_phone_id_set))
    np_list=np.zeros((len(list_phone_id_set),10))

    # get start result array store in np_list
    list_idno=[]
    for i,phone_id_temp in enumerate(list_phone_id_set):

        try:
            np_list[i,0]=int(phone_id_temp)
            list_idno.append("0")
        except Exception as e:
            np_list[i,0]=0
        # print(np_list[i])

    print("np_list")

    #遍历文本
    temp_num=0
    fr_in2=open(text_in)
    for line in fr_in2.readlines():
        stringArr=line.strip().split("\t")
        phone_id=stringArr[1]
        cabin=stringArr[5]
        idcardtype=stringArr[4]

        idcardno=stringArr[3]
        phone_number=stringArr[2]

        # print(line)
        temp_num=temp_num+1
        print(temp_num)
        for i,num in enumerate(np_list):
            # print(int(np_list[i][0]),int(phone_id))

            try:
                if str(int(np_list[i][0]))==phone_id:
                    list_idno[i]=idcardno
                    if cabin=="F":
                        np_list[i][1]=int(np_list[i][1])+1
                    elif (cabin=="C" or cabin=="J"):
                        np_list[i][2]=int(np_list[i][2])+1
                    elif cabin=="Y":
                        np_list[i][3]=int(np_list[i][3])+1
                    else:
                        pass

                    if idcardtype=="0":
                        pass
                    else:
                        np_list[i][4]=int(np_list[i][4])+1


                    if np_list[i][6]==0 and len(phone_number)==11:
                        np_list[i][6]=int(phone_number)


                    if np_list[i][7]==0 and idcardtype=="0" and len(idcardno)==18:
                        try:
                            np_list[i][8]=2015-int(idcardno[6:10])
                            np_list[i][9]=int(idcardno[16:17])%2
                        except Exception as e:
                            pass

                    list_idno[i]=idcardno
            except Exception as e:
                error_out.write(line+"\n")
                print(line)

            # try:
            #     if np_list[i][6]==0 and len(phone_number)==11:
            #         np_list[i][6]=int(phone_number)
            #
            #     if np_list[i][7]==0 and idcardtype=="0" and len(idcardno)==18:
            #         print(idcardno)
            #         np_list[i][7]=idcardno
            #         np_list[i][8]=2015-int(idcardno[6:10])
            #         np_list[i][9]=int(idcardno[16:17])%2
            # except Exception as e:
            #     error_out.write(line+"\n")
            #     print(line)


                # print(int(np_list[i][0]),int(phone_id))
                # temp_num=temp_num+1
        # print(temp_num)
        # if cabin==F
    for i,line in enumerate(np_list):
        string_out1=str(int(np_list[i][0]))+"\t"+str(int(np_list[i][1]))+"\t"+str(int(np_list[i][2]))+"\t"+str(int(np_list[i][3]))+"\t"+str(int(np_list[i][4]))+"\t"+str(int(np_list[i][5]))
        string_out2=str(int(np_list[i][6]))+"\t"+list_idno[i]+"\t"+str(int(np_list[i][8]))+"\t"+str(int(np_list[i][9]))
        string_out=string_out1+"\t"+string_out2
        result_output.write(string_out+"\n")

    print(np_list)


def text_list_set_newtest(text_in="data/ticket_cabinF.txt",text_out="listset/ticket_SH_set_new0127.txt"):
    error="listset/ticket_SH_static_error.txt"
    fr_in=open(text_in)
    result_output=open(text_out,'w')
    error_out=open(error,'w')
    i=0
    list_phone_id=[]
    #get distinct phone_id
    for line in fr_in.readlines():

        stringArr=line.strip().split("\t")

        phone_id=stringArr[1]
        list_phone_id.append(phone_id)
        i=i+1
    # print(i)
    list_phone_id_set=set(list_phone_id)
    # print(len(list_phone_id_set))
    np_list=np.zeros((len(list_phone_id_set),10))

    # get start result array store in np_list
    list_idno=[]
    for i,phone_id_temp in enumerate(list_phone_id_set):

        try:
            np_list[i,0]=int(phone_id_temp)
            list_idno.append("0")
        except Exception as e:
            np_list[i,0]=0
        # print(np_list[i])

    print("np_list")

    #遍历文本
    temp_num=0
    fr_in2=open(text_in)
    for line in fr_in2.readlines():
        stringArr=line.strip().split("\t")
        phone_id=stringArr[1]
        cabin=stringArr[5]
        idcardtype=stringArr[4]

        idcardno=stringArr[3]
        phone_number=stringArr[2]

        # print(line)
        temp_num=temp_num+1
        print(temp_num)
        for i,num in enumerate(np_list):
            # print(int(np_list[i][0]),int(phone_id))

            try:
                if str(int(np_list[i][0]))==phone_id:
                    list_idno[i]=idcardno
                    if cabin=="F":
                        np_list[i][1]=int(np_list[i][1])+1
                    elif (cabin=="C" or cabin=="J"):
                        np_list[i][2]=int(np_list[i][2])+1
                    elif cabin=="Y":
                        np_list[i][3]=int(np_list[i][3])+1
                    else:
                        pass

                    if idcardtype=="0":
                        pass
                    else:
                        np_list[i][4]=int(np_list[i][4])+1


                    if np_list[i][6]==0 and len(phone_number)==11:
                        np_list[i][6]=int(phone_number)


                    if np_list[i][7]==0 and idcardtype=="0" and len(idcardno)==18:
                        try:
                            np_list[i][8]=2015-int(idcardno[6:10])
                            np_list[i][9]=int(idcardno[16:17])%2
                        except Exception as e:
                            pass

                    list_idno[i]=idcardno
            except Exception as e:
                error_out.write(line+"\n")
                print(line)

            # try:
            #     if np_list[i][6]==0 and len(phone_number)==11:
            #         np_list[i][6]=int(phone_number)
            #
            #     if np_list[i][7]==0 and idcardtype=="0" and len(idcardno)==18:
            #         print(idcardno)
            #         np_list[i][7]=idcardno
            #         np_list[i][8]=2015-int(idcardno[6:10])
            #         np_list[i][9]=int(idcardno[16:17])%2
            # except Exception as e:
            #     error_out.write(line+"\n")
            #     print(line)


                # print(int(np_list[i][0]),int(phone_id))
                # temp_num=temp_num+1
        # print(temp_num)
        # if cabin==F
    for i,line in enumerate(np_list):
        string_out1=str(int(np_list[i][0]))+"\t"+str(int(np_list[i][1]))+"\t"+str(int(np_list[i][2]))+"\t"+str(int(np_list[i][3]))+"\t"+str(int(np_list[i][4]))+"\t"+str(int(np_list[i][5]))
        string_out2=str(int(np_list[i][6]))+"\t"+list_idno[i]+"\t"+str(int(np_list[i][8]))+"\t"+str(int(np_list[i][9]))
        string_out=string_out1+"\t"+string_out2
        result_output.write(string_out+"\n")

    print(np_list)

def numpy_cal(text_in="listset/ticket_SH_static.txt",text_out="array/ticket_SH_out.txt"):
    fr_in=open(text_in)
    t=int(len(fr_in.readlines()))
    result_output=open(text_out,'a')

    np_list=np.zeros((t,6))

    fr_in2=open(text_in)
    for i,line in enumerate(fr_in2.readlines()):

        stringArr=line.strip().split("\t")

        phone_id=int(stringArr[0])
        cabin_F=int(stringArr[1])
        cabin_C=int(stringArr[2])
        cabin_Y=int(stringArr[3])
        idtype_1=int(stringArr[4])
        print(phone_id)

        np_list[i][0]=int(phone_id)
        np_list[i][1]=cabin_F
        np_list[i][2]=cabin_C
        np_list[i][3]=cabin_Y
        np_list[i][4]=idtype_1
        np_list[i][5]=cabin_F*5+cabin_C*3+cabin_Y*1+idtype_1*3

    for i,line in enumerate(np_list):
        string_out=str(int(np_list[i][0]))+"\t"+str(int(np_list[i][1]))+"\t"+str(int(np_list[i][2]))+"\t"+str(int(np_list[i][3]))+"\t"+str(int(np_list[i][4]))+"\t"+str(int(np_list[i][5]))
        result_output.write(string_out+"\n")


if __name__=="__main__":
    # text_phone_id_cal()
    # text_cabin_F()
    # text_list_set(text_in="data/ticket_SH.txt",text_out="listset/ticket_SH_static.txt")

    # numpy_cal()
    text_list_set_new0127(text_in="data/ticket_SH.txt",text_out="listset/ticket_SH_last_0127.txt")
    pass