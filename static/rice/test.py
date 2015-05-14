__author__ = 'Administrator'
# from util import logutil
import logging
log = logging.getLogger('test')

temp=0
for i in range(1,1000):
    if (i%11==5) and (i%7==1) and (i%5==2):
        temp=temp+1
        log.log(temp)
        print(i)
print("number is"+" "+str(temp))