from mysql import *
from model import user
from db.mysql import Mysql
import coun_model


class BaseDao(Mysql):

    def __init__(self, dbtype, model):
        Mysql.__init__(self, dbtype=dbtype)
        self.model = model

    def get_results(self, s_day="", end_day="", sql=""):
        results = self.get_all(sql)
        model_list = []
        if not results:
            return []
        for row in results:
            o_model = self.model()
            o_model.setVale(row)
            model_list.append(o_model)
        return model_list

    def result_to_txt(self, file_out_path, s_day="", end_day=""):
        results = self.get_results(s_day=s_day, end_day=end_day)
        file_out = open(file_out_path, "a")
        for o_model in results:
            file_out.write(o_model.getString() + "\n")
        return file_out_path



class CouponDao(BaseDao):
    def __init__(self):
        BaseDao.__init__(self, "hbgj79_account", coun_model.CouponId)

    def get_results(self, s_day="", end_day="", sql=""):
        if s_day == "" and end_day == "" and sql == "":
            sql = "SELECT account,amount,coupon_id FROM coupon where DATE_FORMAT(updatetime,'%Y%m%d')='20150401' and used=1 limit 100"

        elif sql == "":
            sql = "SELECT account,amount,coupon_id FROM coupon " \
                  "where DATE_FORMAT(updatetime,'%%Y%%m%%d')>='%s' " \
                  "and DATE_FORMAT(updatetime,'%%Y%%m%%d')<'%s' and used=1 " % (s_day, end_day)
        print(sql)
        results = super(CouponDao, self).get_results(sql=sql)
        return results

    def result_to_txt(self, file_out_path, s_day="", end_day=""):
        file_path = super(CouponDao, self).result_to_txt(file_out_path=file_out_path, s_day=s_day, end_day=end_day)
        return file_path


class ConsumersDao(BaseDao):
    def __init__(self):
        BaseDao.__init__(self, "hbgj79", coun_model.ConsumersId)

    def get_results(self, s_day="", end_day="", sql=""):
        if s_day == "" and end_day == "" and sql == "":
            sql = "SELECT phoneid from TICKET_ORDER " \
                  "where ORDERSTATUE not in (2,12,21,51,75) " \
                  "and DATE_FORMAT(createtime,'%Y%m%d')='20150401' "

        elif sql == "":
            sql = "SELECT phoneid from TICKET_ORDER " \
              "where ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')>='%s' " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')<'%s'  " %(s_day, end_day)

        print(sql)
        results = super(ConsumersDao, self).get_results(sql=sql)
        return results

    def result_to_txt(self, file_out_path, s_day="", end_day=""):
        file_path = super(ConsumersDao, self).result_to_txt(file_out_path=file_out_path, s_day=s_day, end_day=end_day)
        return file_path


class NewConsumersDao(BaseDao):
    def __init__(self):
        BaseDao.__init__(self, "hbgj79", coun_model.ConsumersId)

    def get_results(self, s_day="", end_day="", sql=""):
        if s_day == "" and end_day == "" and sql == "":
            sql =  "SELECT phoneid from TICKET_ORDER " \
              "where ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(createtime,'%Y%m%d')>='20150401' " \
              "and  phoneid not in " \
              "(select phoneid " \
              "from TICKET_ORDER " \
              "where ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(createtime,'%Y%m%d')< '20150401' ) "

        elif sql == "":
            sql =  "SELECT phoneid from TICKET_ORDER " \
              "where ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')>='%s' " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')<'%s' " \
              "and  phoneid not in " \
              "(select phoneid " \
              "from TICKET_ORDER " \
              "where ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')< %s ) " % (s_day, end_day, s_day)
        print(sql)
        results = super(NewConsumersDao, self).get_results(sql=sql)
        return results

    def result_to_txt(self, file_out_path, s_day="", end_day=""):
        file_path = super(NewConsumersDao, self).result_to_txt(file_out_path=file_out_path, s_day=s_day, end_day=end_day)
        return file_path


def test():
    # sql = "SELECT account,amount FROM coupon where DATE_FORMAT(updatetime,'%Y%m%d')='20150401' limit 100"
    # o_coupon = CouponDao()
    # o_consumer = ConsumersDao()
    o_newsonsumer =NewConsumersDao()
    # results=o_coupon.result_to_txt(file_out_path="test.txt", s_day="20150101", end_day="20150201")
    # result = o_consumer.result_to_txt("consu.txt")
    result = o_newsonsumer.result_to_txt("newconsu.txt")

def getConumain():
    o_coupon = CouponDao()
    result = o_coupon.result_to_txt(file_out_path="coupon_0101_0201", s_day="20150101", end_day="20150201")
    result = o_coupon.result_to_txt(file_out_path="coupon_0201_0301", s_day="20150201", end_day="20150301")
    result = o_coupon.result_to_txt(file_out_path="coupon_0301_0401", s_day="20150301", end_day="20150401")

def getConsumers():
    o_consumer = ConsumersDao()
    result = o_consumer.result_to_txt(file_out_path="consumer_0101_0201", s_day="20150101", end_day="20150201")
    result = o_consumer.result_to_txt(file_out_path="consumer_0201_0301", s_day="20150201", end_day="20150301")
    result = o_consumer.result_to_txt(file_out_path="consumer_0301_0401", s_day="20150301", end_day="20150401")

def getNewConsumers():
    o_newconsumer = NewConsumersDao()
    result = o_newconsumer.result_to_txt(file_out_path="newconsumer_0101_0201", s_day="20150101", end_day="20150201")
    result = o_newconsumer.result_to_txt(file_out_path="newconsumer_0201_0301", s_day="20150201", end_day="20150301")
    result = o_newconsumer.result_to_txt(file_out_path="newconsumer_0301_0401", s_day="20150301", end_day="20150401")


if __name__ == "__main__":
    # test()
    # getConumain()
    # getConsumers()
    getNewConsumers()