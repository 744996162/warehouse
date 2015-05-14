#ecoding=utf-8
__author__ = 'Administrator'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import jieba


def jieba_return_list4(str_in):
    # test="湖北省武汉市武昌区中北路31号楚河汉街工行知音大厦（2号门进）19楼"
    list_str=[]
    result_list= jieba.cut(str_in)
    list_str.append(result_list.next())
    list_str.append(result_list.next())
    list_str.append(result_list.next())

    string_temp2=""
    result_list2= jieba.cut(str_in)
    for (i,str) in enumerate(result_list2):
        if i<3:
            string_temp2=string_temp2+str+" "
        else:
            string_temp2=string_temp2+str
            # string_temp=string_temp+i+"\t"
    list_str.append(string_temp2)

    # print list_str[0],list_str[1],list_str[2],list_str[3]
    return list_str

def jieba_return_list5(str_in):
    # test="湖北省武汉市武昌区中北路31号楚河汉街工行知音大厦（2号门进）19楼"
    list_str=[]
    result_list= jieba.cut(str_in)
    list_str.append(result_list.next())
    list_str.append(result_list.next())
    list_str.append(result_list.next())

    string_temp1=""
    string_temp2=""
    result_list2= jieba.cut(str_in)
    for (i,str) in enumerate(result_list2):
        if i<3:
            string_temp1=string_temp1+str+" "
        else:
            string_temp1=string_temp1+str
            string_temp2=string_temp2+str
            # string_temp=string_temp+i+"\t"
    list_str.append(string_temp1)
    list_str.append(string_temp2)
    # print list_str[0],list_str[1],list_str[2],list_str[3]
    return list_str

def text_rice(text_in="data/gift_order_0126.txt",text_out="data/out_0126.txt"):
    fr_in=open(text_in)
    result_output=open(text_out,'w')
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")

        order_id=stringArr[0]
        phone_id=stringArr[1]

        json_string=stringArr[2]
        json_obj= json.loads(stringArr[2])
        name=json_obj["name"]
        phone=json_obj["phone"]
        address=json_obj["address"]

        createtime=stringArr[3]

        string_out=order_id+"\t"+phone_id+"\t"+name+"\t"+phone+"\t"+address+"\t"+createtime
        result_output.write(string_out+"\n")

        print(string_out)
        # name=json_str["name"]
        # print(json_str)
    return text_out
    pass


def text_string_jieba(text_in="data/out_0126.txt",text_out="data/jieba_out.txt",string_num=3):
    fr_in=open(text_in)
    result_output=open(text_out,'w')
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")

        order_id=stringArr[0]
        phone_id=stringArr[1]
        name=stringArr[2]
        phone=stringArr[3]
        createtime=stringArr[5]

        address=stringArr[4]
        result_list= jieba.cut(address)  # 默认是精确模式
        string_temp=""
        string_temp1=""
        string_temp2=""
        for (i,str) in enumerate(result_list):
            # print(i,str)
            if i<3:
                string_temp1=string_temp1+str+"\t"
                string_temp2=string_temp2+str+" "
            else:
                string_temp2=string_temp2+str
            # string_temp=string_temp+i+"\t"
        print string_temp1,string_temp2
        string_out=order_id+"\t"+name+"\t"+string_temp1+string_temp2+"\t"+phone+"\t"+createtime
        result_output.write(string_out+"\n")


def text_string_jieba2(text_in="data/out_0126.txt",text_out="data/jieba_out.txt",error_out="data/error.txt"):
    fr_in=open(text_in)
    result_output=open(text_out,'w')
    error_output=open(error_out,'w')
    for line in fr_in.readlines():
        try:
            stringArr=line.strip().split("\t")

            order_id=stringArr[0]
            phone_id=stringArr[1]
            name=stringArr[2]
            phone=stringArr[3]
            createtime=stringArr[5]

            address=stringArr[4]

            result_list4=jieba_return_list4(address)

            sheng=str(result_list4[0])
            shi=result_list4[1]
            qu=result_list4[2]
            address_all=result_list4[3]
            # print sheng,shi,qu,address_all

            string_out=order_id+"\t"+name+"\t"+sheng+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime

            if (("省" in sheng) or ("自治区" in sheng)) and ("市" in shi) and ("区" in qu) and ("市辖" not in qu):
                result_output.write(string_out+"\n")
            elif ("北京" in sheng):
                string_out=order_id+"\t"+name+"\t"+"北京"+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                error_output.write(string_out+"\n")
            elif ("天津" in sheng):
                string_out=order_id+"\t"+name+"\t"+"天津"+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                error_output.write(string_out+"\n")
            elif ("上海" in sheng):
                string_out=order_id+"\t"+name+"\t"+"上海"+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                error_output.write(string_out+"\n")
            elif ("重庆" in sheng):
                string_out=order_id+"\t"+name+"\t"+"重庆"+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                error_output.write(string_out+"\n")
            else:
                # if ("市" in sheng) and ("区" in shi):
                #     string_out=order_id+"\t"+name+"\t"+""+"\t"+sheng+"\t"+shi+"\t"+address_all+"\t"+phone+"\t"+createtime
                #     pass
                error_output.write(string_out+"\n")
                pass
        except Exception as e:
            print(line)
            continue
    return text_out,error_out


def text_string_jieba3(text_in="data/out_0126.txt",text_out="data/jieba_out.txt",error_out="data/error.txt"):
    fr_in=open(text_in)
    result_output=open(text_out,'w')
    error_output=open(error_out,'w')
    for line in fr_in.readlines():
        try:
            stringArr=line.strip().split("\t")

            order_id=stringArr[0]
            phone_id=stringArr[1]
            name=stringArr[2]
            phone=stringArr[3]
            createtime=stringArr[5]

            address=stringArr[4]

            result_list5=jieba_return_list5(address)

            sheng=str(result_list5[0])
            shi=result_list5[1]
            qu=result_list5[2]
            address_all=result_list5[3]
            address_after=result_list5[4]
            # print sheng,shi,qu,address_all

            string_out=order_id+"\t"+name+"\t"+sheng+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime

            if (("省" in sheng) or ("自治区" in sheng)) and ("市" in shi) and ("区" in qu) and ("市辖" not in qu):
                result_output.write(string_out+"\n")

            elif ("北京" in sheng):
                if (("区" in qu) and ("市辖" not in qu)):
                    sheng="北京"
                    shi="北京市"
                    address_all=sheng+" "+shi+" "+qu+" "+address_after
                    string_out=order_id+"\t"+name+"\t"+sheng+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                    result_output.write(string_out+"\n")
                else:
                    temp=qu
                    qu=shi
                    sheng="北京"
                    shi="北京市"
                    address_all=sheng+" "+shi+" "+qu+" "+temp+address_after
                    string_out=order_id+"\t"+name+"\t"+sheng+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                    error_output.write(string_out+"\n")
            elif ("上海" in sheng):
                if (("区" in qu) and ("市辖" not in qu)):
                    sheng="上海"
                    shi="上海市"
                    address_all=sheng+" "+shi+" "+qu+" "+address_after
                    string_out=order_id+"\t"+name+"\t"+sheng+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                    result_output.write(string_out+"\n")
                else:
                    temp=qu
                    qu=shi
                    sheng="上海"
                    shi="上海市"
                    address_all=sheng+" "+shi+" "+qu+" "+temp+address_after
                    string_out=order_id+"\t"+name+"\t"+sheng+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                    error_output.write(string_out+"\n")
            elif ("重庆" in sheng):
                if (("区" in qu) and ("市辖" not in qu)):
                    sheng="重庆"
                    shi="重庆市"
                    address_all=sheng+" "+shi+" "+qu+" "+address_after
                    string_out=order_id+"\t"+name+"\t"+sheng+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                    result_output.write(string_out+"\n")
                else:
                    temp=qu
                    qu=shi
                    sheng="重庆"
                    shi="重庆市"
                    address_all=sheng+" "+shi+" "+qu+" "+temp+address_after
                    string_out=order_id+"\t"+name+"\t"+sheng+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                    error_output.write(string_out+"\n")
            elif ("天津" in sheng):
                if (("区" in qu) and ("市辖" not in qu)):
                    sheng="天津"
                    shi="天津市"
                    address_all=sheng+" "+shi+" "+qu+" "+address_after
                    string_out=order_id+"\t"+name+"\t"+sheng+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                    result_output.write(string_out+"\n")
                else:
                    temp=qu
                    qu=shi
                    sheng="天津"
                    shi="天津市"
                    address_all=sheng+" "+shi+" "+qu+" "+temp+address_after
                    string_out=order_id+"\t"+name+"\t"+sheng+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                    error_output.write(string_out+"\n")
            else:
                if ("市" in sheng):
                    temp_shi=shi
                    temp_qu=qu
                    shi=sheng
                    sheng=""
                    qu=""
                    address_all=shi+" "+temp_shi+temp_qu+address_after
                if (((len(qu)<=2) or ("路" in qu) or (("县") not in qu) or (("市") not in qu)) and qu!="" ):
                    address_all=sheng+" "+shi+" "+qu+address_after
                    qu=""

                string_out=order_id+"\t"+name+"\t"+sheng+"\t"+shi+"\t"+qu+"\t"+address_all+"\t"+phone+"\t"+createtime
                error_output.write(string_out+"\n")
                pass
        except Exception as e:
            print(line)
            continue
    return text_out,error_out

if __name__=="__main__":
    # text_phone_id_cal()
    # text_cabin_F()

    # jieba_returnlist("w")
    # text_rice()
    # text_string_jieba()

    test="湖北省武汉市武昌区中北路31号楚河汉街工行知音大厦（2号门进）19楼"
    t=jieba_return_list5(test)
    print t[0],t[1],t[2],t[3],t[4]
    # text_string_jieba2()
    pass