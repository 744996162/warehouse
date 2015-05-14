#coding=utf-8
__author__ = 'zhangchao'

class City(object):
    def __init__(self):
        self.airport_table = "city_code"
        # self.fr_in=open(airport_table)

    def getCityCode(self, city_name):
        # airport_table="city_code"
        fr_in = open(self.airport_table)
        for line in fr_in.readlines():
            stringArr = line.strip().split("\t")
            if stringArr[0] == city_name:
                return stringArr[1]
        return 0

    def getCityList(self):
        fr_in = open(self.airport_table)
        city_list = []
        for line in fr_in.readlines():
            stringArr = line.strip().split("\t")
            if stringArr != "":
                city_list.append(stringArr[1])
        return city_list

    def getTwoCityList(self):
        two_city_list = []
        t = self.getCityList()
        for i in t:
            for j in t:
                if i != j:
                    two_city_list.append([i,j])
        return two_city_list


if __name__ == "__main__":
    city = City()
    city_1 = city.getCityCode("武汉")
    city_2 = city.getCityList()
    city_list = city.getTwoCityList()
    print(city_1)
    print(city_2)
    print(city_list)
    pass