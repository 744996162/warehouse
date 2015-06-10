__author__ = 'Administrator'
from source_hbgj_oracle import oracle_con
from domain.model import ActiveId
from domain.model import NewUsersId


class BaseUserOracleDao(object):
    def __init__(self):
        self.cursor = oracle_con()

    def query_result_by_setValue(self, sql, model_class):
        cursor = self.cursor
        cursor.execute(sql)
        result = cursor.fetchall()
        users_model_list = []
        if not result:
            return False
        for row in result:
            value_list = []
            for value in row:
                value_list.append(value)
            o_model = model_class()
            o_model.setValues(value_list)
            users_model_list.append(o_model)
        return users_model_list


class ActiveIdDao(object):
    def __init__(self, DBClass=BaseUserOracleDao, ModelClass=ActiveId):
        self.db = DBClass()
        self.ModelClass = ModelClass

    def get_id(self, s_start_day, s_end_day):
        sql = "select distinct userid " \
        "from ACTIVE_USER_LOG " \
        "where createtime>=to_date(%s,'yyyymmdd') " \
        "and createtime<to_date(%s,'yyyymmdd') "  %(s_start_day, s_end_day)

        result_model_list=self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

    def get_id_to_txt(self,s_start_day, s_end_day, file_path=""):
        if file_path == "":
            file_path = "active" + s_start_day[0:6]
        file_out = open(file_path, "a")
        result_list = self.get_id(s_start_day, s_end_day)
        for model in result_list :
            file_out.write(str(model.uid)+"\n")
        pass

    def get_id_set(self, s_start_day, s_end_day):
        result_list = self.get_id(s_start_day, s_end_day)
        uid_list = []
        for model in result_list :
            uid_list.append(model.uid)
        return set(uid_list)


class NewUsersDao(object):
    def __init__(self, DBClass = BaseUserOracleDao, ModelClass=NewUsersId):
        self.db = DBClass()
        self.ModelClass =ModelClass

    def get_id(self, s_start_day, s_end_day):
        ''' querydate_str = "20150401" '''

        sql = "select distinct user_id from HBZJ_USER   " \
              "where USER_LOGINDATE>=to_date(%s,'yyyymmdd') " \
              "and USER_LOGINDATE<to_date('%s','yyyymmdd')  " %(s_start_day, s_end_day)

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

    def get_id_ios(self, s_start_day, s_end_day):
        ''' querydate_str = "20150401" '''

        sql = "select distinct user_id from HBZJ_USER   " \
              "where USER_LOGINDATE>=to_date(%s,'yyyymmdd') " \
              "and USER_LOGINDATE<to_date('%s','yyyymmdd')  " \
              "and (USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%') "  %(s_start_day, s_end_day)

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list


    def get_id_set(self, s_start_day, s_end_day):
        ''' querydate_str = "20150401" '''

        result_list = self.get_id(s_start_day, s_end_day)
        uid_list = []
        for model in result_list :
            uid_list.append(model.uid)
        return set(uid_list)


    def get_id_ios_set(self, s_start_day, s_end_day):
        ''' querydate_str = "20150401" '''
        result_list = self.get_id_ios(s_start_day, s_end_day)
        uid_list = []
        for model in result_list:
            uid_list.append(model.uid)
        return set(uid_list)

def testActiveId():
    o_ActiveIdDao = ActiveIdDao()
    o_ActiveIdDao.get_id_to_txt("20150401", "20150501", "active201504")
    pass


def lcd():
    file_out = open("lcd_result201505.data", "a")
    o_ActiveIdDao = ActiveIdDao()
    active_set = o_ActiveIdDao.get_id_set("20150501", "20150601")

    s_list = ["20150401", "20150301", "20150201", "20150101", "20141201", "20141101", "20141001", "20140901", "20140801", "20140701", "20140601", "20140501", "20140401", "20140301", "20140201", "20140101"]
    e_list = ["20150501", "20150401", "20150301", "20150201", "20150101", "20141201", "20141101", "20141001", "20140901", "20140801", "20140701", "20140601", "20140501","20140401", "20140301", "20140201"]

    for num, value in enumerate(s_list):
        print(s_list[num], e_list[num])
        o_NewUsersDao = NewUsersDao()
        new_User_set = o_NewUsersDao.get_id_set(s_list[num], e_list[num])
        new_User_set_ios = o_NewUsersDao.get_id_ios_set(s_list[num], e_list[num])
        all_num = str(len(active_set & new_User_set))
        ios_num = str(len(active_set & new_User_set_ios))
        android_num = str(int(all_num)-int(ios_num))
        file_out.write(str(s_list[num]) + "\t" + all_num + "\t" + str(ios_num) + "\t" + str(android_num) + "\n")
        print("all:" + str(all_num))
        print("ios:" + str(ios_num))

    # o_NewUsersDao = NewUsersDao()
    # new_User_set201503 = o_NewUsersDao.get_id_set("20150301", "20150401")
    # new_User_set201503_ios = o_NewUsersDao.get_id_ios_set("20150301", "20150401")
    #
    # print("all:" + str(len(active_set201504 & new_User_set201503)))
    # print("ios:" + str(len(active_set201504 & new_User_set201503_ios)))


    pass
if __name__ == "__main__":
    # testActiveId()
    lcd()
    pass