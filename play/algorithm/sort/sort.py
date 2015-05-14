#ecoding=utf-8
__author__ = 'Administrator'
import random


def rand_list(ran_num=10000):
    list_temp = []
    for i in range(ran_num):
        list_temp.append(random.randint(0, ran_num))
    return list_temp


def list_check(_list):
    for i in range(0, len(_list)-1):
        if _list[i] > _list[i+1]:
            return False
    return True


def select_sort(list2):
    if list2 == [] or len(list2)<2:
        return list2
    for i in range(0, len(list2)):
        min = i
        for j in range(i + 1, len(list2)):
            if list2[j] < list2[min]:
                min = j
        list2[i], list2[min] = list2[min], list2[i]
    return list2


def insert_sort(list):
    if list == [] or len(list)<2:
        return list
    pass
    for i in range(0, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
        pass
    return list


def mao_pao_sort(_list):
    for i in range(0, len(_list)):
        for j in range(1, len(_list)-i):
            if _list[j-1] > _list[j]:
                _list[j-1], _list[j] = _list[j+1], _list[j]
                pass
            pass
    return list
    pass


def gui_bing_sort2(l_list, r_list):
    l_len = len(l_list)
    r_len = len(r_list)
    #归队结束时间：[]和else
    if l_len+r_len < 2:
        return l_list+r_list
    l_rst = gui_bing_sort2(l_list[:l_len/2], l_list[l_len/2:l_len])
    r_rst = gui_bing_sort2(r_list[:r_len/2], r_list[r_len/2:r_len])
    lcursor, rcursor = 0, 0
    result = []
    min_len = min(l_len, r_len)
    #from litter to bigger
    while lcursor < l_len and rcursor < r_len:
        if l_rst[lcursor] < rcursor[rcursor]:
            result.append(l_rst[lcursor])
            lcursor += 1
        else:
            result.append(r_rst[rcursor])
            rcursor += 1
    result.extend(l_rst[lcursor])
    result.extend(r_rst[rcursor])
    return result



    pass


def gui_bing_main(_list):
    l_len = len(_list)
    return gui_bing_sort2(_list[:l_len/2], _list[l_len/2:l_len])


def test():
    list_temp = [1, 2, 2, 4, 3]
    list_temp.sort()
    print(list_temp)

if __name__=="__main__":
    # t = rand_list(100)
    # print(t)
    # print(list_check(t))
    # # t2 = select_sort(t)
    # t2 = maopao_sort(t)
    # print(t2)
    # print(list_check(t2))
    # test()
    t = rand_list(5)
    print(t)
    print(gui_bing_main(t))




