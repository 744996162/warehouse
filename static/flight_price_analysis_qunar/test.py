#coding=utf-8
__author__ = 'Administrator'
import random
import matplotlib.pyplot as plt

def test():

    red=random.randint(11,99)

    guess1=random.randint(11,99)

def guess_program(start, end,red,guess_num=1):

    guess_temp=random.randint(start,end)
    # print(guess_temp)
    if guess_temp==red:
        return guess_temp,guess_temp,guess_temp,guess_num
    elif guess_temp>red:
        return guess_program(start,guess_temp-1,red,guess_num+1)

    elif guess_temp<red:
        return guess_program(guess_temp+1,end,red,guess_num+1)


def guess_program_half(start,end,red,guess_num=1):
    guess_temp=(start+end)/2
    print(guess_temp)
    if guess_temp==red:
        return guess_temp,guess_temp,guess_temp,guess_num
    elif guess_temp>red:
        return guess_program(start,guess_temp-1,red,guess_num+1)

    elif guess_temp<red:
        return guess_program(guess_temp+1,end,red,guess_num+1)


def count_list_num(list,num):
    temp_num=0
    for i in list:
        if num==i:
            temp_num=temp_num+1
    return temp_num

def guess1():
    start=10
    end=99
    red_list=[]
    guess_num_list=[]
    average_red_list=[]

    for temp in range(1,100000):
        rand_temp=random.uniform(-0.25,0.25)
        red=random.randint(10,99)
        start_temp,end_temp,red_temp,num=guess_program(start,end,red)

        red_list.append((red+rand_temp))
        guess_num_list.append(num)
        average_red_list.append(round(red)/num)

    for i in range(1,40):
        count=count_list_num(guess_num_list,i)
        count_all=len(guess_num_list)
        print(i,count,"%.2f%%"  % (round(count)/count_all*100))
    pass

def guess2():
    start=10
    end=99
    red_list=[]
    guess_num_list=[]
    average_red_list=[]

    for temp in range(1,1000):
        rand_temp=random.uniform(-0.25,0.25)

        red=random.randint(10,99)
        print(red)
        start_temp,end_temp,red_temp,num=guess_program_half(start,end,red)

        red_list.append((red+rand_temp))
        guess_num_list.append(num)
        average_red_list.append(round(red)/num)

    for i in range(1,40):
        count=count_list_num(guess_num_list,i)
        count_all=len(guess_num_list)
        print(i,count,"%.2f%%"  % (round(count)/count_all*100))
    pass





if __name__=="__main__":
    # guess1()
    guess2()
