__author__ = 'Administrator'

class BaseModel(object):
    def __init__(self):
        pass

    def __str__(self):
        pass

    def getFieldList(self):
        return []

    def setValue(self):
        fileList = self.getFieldList()


class OrderModel(object):
    def __init__(self):
        self.uid = ''
        self.order_date = ''
        self.depart_date = ''
        self.depart_name = ''
        self.arrive_name = ''
        self.ticket_count = ''
        self.train_no = ''

    def setValue(self,uid, order_date, depart_date, depart_name, arrive_name, ticket_count, train_no):
        self.uid = uid
        self.order_date = order_date
        self.depart_date = depart_date
        self.depart_name = depart_name
        self.arrive_name = arrive_name
        self.ticket_count = ticket_count
        self.train_no = train_no

    def __str__(self):
        return "OrderModel:" + "\t" + str(self.uid)





