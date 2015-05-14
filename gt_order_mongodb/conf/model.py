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

    def setVale(self,  uid, p_info, account, order_date,
                i_status, depart_date, depart_name, arrive_name, ticket_count, train_no, amount, create_time):
        self.uid = uid
        self.p_info = p_info
        self.account = account
        self.order_date = order_date
        self.i_status = i_status
        self.depart_date = depart_date
        self.depart_name = depart_name
        self.arrive_name = arrive_name
        self.ticket_count = ticket_count
        self.train_no = train_no
        self.amount = amount
        self.create_time = create_time

    def __str__(self):
        str_out = "Orders:" + "\t" + self.uid + "\t" + str(self.create_time)
        return str_out

    def getString(self):
        str = self.uid + "\t" + self.p_info + "\t" + self.account + "\t" + self. order_date + "\t" \
              + self.i_status + "\t" + self. depart_date + "\t" + self. depart_name + "\t" \
              + self. arrive_name + "\t" + self. ticket_count + "\t" + self. train_no + "\t" + self. amount + "\t" + self. create_time
        return str


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


    def setVale(self, order_id, uid, account, p_info, depart_date, train_no,
                depart_name, arrive_name, name, card_type, card_no, phone, seat_name,
                ticket_type, status, price, create_time):
        self.order_id = order_id
        self.uid = uid
        self.account = account
        self.p_info = p_info
        self.depart_date = depart_date
        self.train_no = train_no
        self.depart_name = depart_name
        self.arrive_name = arrive_name
        self.name = name
        self.card_type = card_type
        self.card_no = card_no
        self.phone = phone
        self.seat_name = seat_name
        self.ticket_type = ticket_type
        self.status = status
        self.price = price
        self.create_time = create_time

    def __str__(self):
        str_out = "OrderSub:" + "\t" + self.uid + "\t" + str(self.create_time)
        return str_out

    def getString(self):

        str = self.order_id + "\t" + self.uid + "\t" + self.account + "\t" + self.p_info + "\t" + self.depart_date \
               + "\t" + self.train_no + "\t" + self.depart_name + "\t" + self.arrive_name + "\t" + self.name \
               + "\t" + self.card_type + "\t" + self.card_no + "\t" + self.phone + "\t" + self.seat_name \
               + "\t" + self.ticket_type + "\t" + self.status + "\t" + self.price + "\t" + self.create_time
        return str
