__author__ = 'Administrator'

class Model_Order():
    def __init__(self):
        self.uid = ""
        self.p_info = ""
        self.account = ""
        self.order_date = ""
        self.i_status = ""
        self.depart_date = ""
        self.depart_name = ""
        self.arrive_name = ""
        self.ticket_count = ""
        self.train_no = ""
        self.amount = ""
        self.create_time = ""

        self.pay_method = ""
        self.pay_time = ""


    def setValue(self, value_list):
        self.uid = str(value_list[0])
        self.p_info = str(value_list[1])
        self.account = str(value_list[2])
        self.order_date = str(value_list[3])
        self.i_status = str(value_list[4])
        self.depart_date = str(value_list[5])
        self.depart_name = str(value_list[6])
        self.arrive_name = str(value_list[7])
        self.ticket_count = str(value_list[8])
        self.train_no = str(value_list[9])
        self.amount = str(value_list[10])
        self.create_time = str(value_list[11])
        
        self.pay_method = str(value_list[12])
        self.pay_time = str(value_list[13])

    def __str__(self):
        str_out = "Orders:" + "\t" + self.uid + "\t" + str(self.create_time)
        return str_out

    def getString(self):
        str = self.uid + "\t" + self.p_info + "\t" + self.account + "\t" + self. order_date + "\t" \
              + self.i_status + "\t" + self. depart_date + "\t" + self. depart_name + "\t" \
              + self. arrive_name + "\t" + self. ticket_count + "\t" + self. train_no + "\t" \
              + self. amount + "\t" + self. create_time + "\t" + self.pay_method + "\t" + self.pay_time
        return str

    def getJson(self):
        pass


class Model_OrderSub():
    def __init__(self):
        self.order_id = ""
        self.uid = ""
        self.account = ""
        self.p_info = ""
        self.depart_date = ""
        self.train_no = ""
        self.depart_name = ""
        self.arrive_name = ""
        self.name = ""
        self.card_type = ""
        self.card_no = ""
        self.phone = ""
        self.seat_name = ""
        self.ticket_type = ""
        self.status = ""
        self.price = ""
        self.create_time = ""


    def setVale(self, value_list):
        self.order_id = str(value_list[0])
        self.uid = str(value_list[1])
        self.account = str(value_list[2])
        self.p_info = str(value_list[3])
        self.depart_date = str(value_list[4])
        self.train_no = str(value_list[5])
        self.depart_name = str(value_list[6])
        self.arrive_name = str(value_list[7])
        self.name = str(value_list[8])
        self.card_type = str(value_list[9])
        self.card_no = str(value_list[10])
        self.phone = str(value_list[11])
        self.seat_name = str(value_list[12])
        self.ticket_type = str(value_list[13])
        self.status = str(value_list[14])
        self.price = str(value_list[15])
        self.create_time = str(value_list[16])


    def __str__(self):
        str_out = "OrderSub:" + "\t" + self.uid + "\t" + str(self.create_time)
        return str_out

    def getString(self):

        str = self.order_id + "\t" + self.uid + "\t" + self.account + "\t" + self.p_info + "\t" + self.depart_date \
               + "\t" + self.train_no + "\t" + self.depart_name + "\t" + self.arrive_name + "\t" + self.name \
               + "\t" + self.card_type + "\t" + self.card_no + "\t" + self.phone + "\t" + self.seat_name \
               + "\t" + self.ticket_type + "\t" + self.status + "\t" + self.price + "\t" + self.create_time
        return str
