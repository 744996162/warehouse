#ecoding=utf-8
__author__ = 'Administrator'
import pymongo
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class CityCode():
    def __init__(self):
        self.station_code_dict, self.city_code_dict = self._getDict()
        pass

    def _getDict(self):
        station_info_path = "station_info.txt"
        station_info_file = open(station_info_path)
        station_code_dict = {}
        city_code_dict={}
        for line in station_info_file:
            stringArr=line.strip().split("\t")
            code = stringArr[0]
            name = stringArr[1].encode('gbk')
            city_code = stringArr[2]
            station_code_dict.setdefault(name, code)
            city_code_dict.setdefault(name, city_code)
        return station_code_dict, city_code_dict


    def getStationCode(self, name):
        station_code_dict = self.station_code_dict
        station_code = station_code_dict.get(name.encode('gbk'))
        return station_code
        pass

    def getCityCode(self, name):
        city_code_dict = self.city_code_dict
        city_code = city_code_dict.get(name.encode('gbk'))
        return city_code



if __name__=="__main__":
    # getCityCode()
    o = CityCode()
    # print(o.getCityCode('\xc9\xe1\xc1\xa6\xbb\xa2'))
    # print(o.getStationCode('\xc9\xe1\xc1\xa6\xbb\xa2'))
    print(o.getCityCode("汉口"))
    print(o.getStationCode("汉口"))

