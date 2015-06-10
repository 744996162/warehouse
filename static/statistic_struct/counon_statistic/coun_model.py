__author__ = 'Administrator'
class CouponId(object):

    def __init__(self):
        self.id = ''
        self.price = ''
        self.coupon_id = ''

    def setVale(self, s_list):
        self.id = str(s_list[0])
        self.price = str(s_list[1])
        self.coupon_id = str(s_list[2])

    def __str__(self):
        str_out = "Coupon:" + "\t" + str(self.id) + "\t" + str(self.price)
        return str_out

    def getString(self):
        str_out = str(self.id) + "\t" + str(self.price) + "\t" + str(self.coupon_id)
        return str_out


class CouponIdTime(object):

    def __init__(self):
        self.id = ''
        self.s_day = ''
        self.coupon_id = ''

    def setVale(self, s_list):
        self.id = str(s_list[0])
        self.s_day = str(s_list[1])
        self.coupon_id = str(s_list[2])

    def __str__(self):
        str_out = "CouponTime:" + "\t" + str(self.id) + "\t" + str(self.s_day)
        return str_out

    def getString(self):
        str_out = str(self.id) + "\t" + str(self.s_day) + "\t" + str(self.coupon_id)
        return str_out


class ConsumersId(object):
    def __init__(self):
        self.id = ''
    def setVale(self, s_list):
        self.id = str(s_list[0])
    def __str__(self):
        str_out = "Consumers:" + "\t" + str(self.id)
        return str_out

    def getString(self):
        str_out = str(self.id)
        return str_out