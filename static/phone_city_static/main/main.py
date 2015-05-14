#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from phone.db import city_query
def changedata(in_file,result_file,error_file):
    #查询对象
    query1=city_query.PhoneUserDao()
    #输出文件
    result_output=open(result_file,'w')
    error_output=open(error_file,'w')
    temp_phone_pre=0
    temp_sheng="0"
    temp_shi="0"
    for line in file(in_file):

       phoneid,phone=line.strip().split(',')
       phone_pre=phone[0:7]
       if phone_pre==temp_phone_pre:
           sheng=temp_sheng
           shi=temp_shi
       else:
           try:
                sheng,shi=query1.query_city(int(phone_pre))
           except Exception as e:
                sheng="0"

       if  sheng=="0":
          #输出到error
          text=str(phoneid)+','+str(phone)
          error_output.write(text+'\n')
       else:
          text=str(phoneid)+','+str(phone)+','+sheng+','+shi
          result_output.write(text+'\n')
       temp_phone_pre=phone_pre
       temp_sheng=sheng
       temp_shi=shi
       print temp_shi

def exacte_data(in_file,result_file):
    #查询对象

    query1=city_query.PhoneUserDao()
    query2=city_query.PhoneUserDao()
    #输出文件
    result_output=open(result_file,'w')
    sheng_dongguan,shi_dongguan=query2.query_city(1304682)
    temp_phone_pre=0
    temp_sheng="0"
    temp_shi="0"
    for line in file(in_file):

       phoneid,phone=line.strip().split(',')
       phone_pre=phone[0:7]
       if phone_pre==temp_phone_pre:
           sheng=temp_sheng
           shi=temp_shi
       else:
           try:
                sheng,shi=query1.query_city(int(phone_pre))
           except Exception as e:
                sheng="0"
                shi="0"

       if  shi==shi_dongguan:
          #输出到error
          text=str(phoneid)+','+str(phone)+','+sheng+','+shi
          result_output.write(text+'\n')
       else:
          pass
       temp_phone_pre=phone_pre
       temp_sheng=sheng
       temp_shi=shi
       print temp_shi


def changedata_test():
    infile='phone_user.data'
    resultfile='result.data'
    errorfile='error.data'
    changedata(infile,resultfile,errorfile)

def exacte_data_test():
    infile='phone_user.data'
    resultfile='city_data.data'
    exacte_data(infile,resultfile)

if __name__=="__main__":
    # infile='test_in.txt'
    # resultfile='test_result.txt'
    # errorfile='test_error.txt'
    exacte_data_test()

    print("test")
    pass




