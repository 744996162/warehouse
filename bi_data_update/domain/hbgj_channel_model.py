__author__ = 'Administrator'


class New_users(object):
    def __init__(self):
        self.s_day = ''
        self.channel = ''
        self.new_users = 0

    def getlist(self):
        return ['s_day', 'channel', 'new_users']

    def getValues(self):
        return [self.s_day, self.channel, self.new_users]

    def __str__(self):
        out_str = "HB_New_users:" + "\t" + str(self.channel) + "\t" + self.s_day + "\t" + str(self.new_users)
        return out_str

    def setValues(self,valueList):
        self.s_day = str(valueList[0])
        self.channel = str(valueList[1])
        self.new_users = int(valueList[2])


class New_consumers(object):
    def __init__(self):
        self.s_day = ''
        self.channel = ''
        self.new_consumers = 0

    def getlist(self):
        return ['s_day', 'channel', 'new_consumers']

    def getValues(self):
        return [self.s_day, self.channel, self.new_consumers]

    def setValues(self,valueList):
        self.s_day = str(valueList[0])
        self.channel = str(valueList[1])
        self.new_consumers = int(valueList[2])

    def __str__(self):
        out_str = "HB_New_consumers:" + "\t" + str(self.channel) + "\t" + self.s_day + "\t" + str(self.new_consumers)
        return out_str


class Active_users(object):
    def __init__(self):
        self.s_day = ''
        self.channel = ''
        self.active_users = 0


    def __str__(self):
        out_str = "HB_active_users:" + "\t" + str(self.channel) + "\t" + str(self.s_day) + "\t" + str(self.active_users)
        return out_str

    def getlist(self):
        return ['s_day', 'channel', 'active_users']

    def getValues(self):
        return [self.s_day, self.channel, self.active_users]

    def setValues(self,valueList):
        self.s_day = str(valueList[0])
        self.channel = str(valueList[1])
        self.active_users = int(valueList[2])


class Orders_source(object):
    def __init__(self):
        self.s_day = ''
        self.p = ''
        self.payprice = 0
        self.order_count = 0
        self.ticket_count = 0

    def __str__(self):
        out_str = "Orders_source:" + "\t" + str(self.s_day) + "\t" + str(self.p )+ "\t" + str(self.ticket_count)
        return out_str

    def getlist(self):
        return ['s_day', 'p', 'payprice', 'order_count', 'ticket_count']

    def getValues(self):
        return [self.s_day, self.p, self.payprice, self.order_count, self.ticket_count]

    def setValues(self, valueList):
        self.s_day = str(valueList[0])
        self.p = str(valueList[1])
        self.payprice = float(valueList[2])
        self.order_count = int(valueList[3])
        self.ticket_count = int(valueList[4])


class Orders_goal(object):
    def __init__(self):
        self.s_day = ''
        self.channel = ''
        self.amount = 0
        self.order_count = 0
        self.ticket_count = 0

    def __str__(self):
        out_str = "Orders_goal:" + "\t" + str(self.s_day) + "\t" + str(self.channel) + "\t" + str(self.ticket_count)
        return out_str

    def getlist(self):
        return ['s_day', 'channel', 'amount', 'order_count', 'ticket_count']

    def getValues(self):
        return [self.s_day, self.channel, self.amount, self.order_count, self.ticket_count]

    def setValues(self, valueList):
        self.s_day = str(valueList[0])
        self.channel = str(valueList[1])
        self.amount = float(valueList[2])
        self.order_count = int(valueList[3])
        self.ticket_count = int(valueList[4])



def orderModelList_source_to_goal(order_source_list):
    goal_data_list = []
    for order_source in order_source_list:

        s_day = order_source.s_day
        p = order_source.p
        payprice = order_source.payprice
        order_count = order_source.order_count
        ticket_count = order_source.ticket_count
        channel = p.strip().split(",")[0]
        o_order_goal = Orders_goal()
        o_order_goal.setValues([s_day, channel, payprice, order_count, ticket_count])
        goal_data_list.append(o_order_goal)
    return goal_data_list

def mearge(model1, model2):

    s_day1 = model1.s_day
    channel1 = model1.channel

    s_day2 = model2.s_day
    channel2 = model2.channel

    if s_day1 == s_day2 and channel1 == channel2:
        model1.amount += model2.amount
        model1.order_count += model2.order_count
        model1.ticket_count += model2.ticket_count
        return model1
    else:
        return model1


def meargeList(data_list):
    result_list = []
    channel_set = set()
    for i in range(len(data_list)):
        modeli = data_list[i]
        if (modeli.s_day, modeli.channel) in channel_set:
            continue
        for j in range(i+1, len(data_list)):
            modelj = data_list[j]
            modeli = mearge(modeli, modelj)
        result_list.append(modeli)
        channel_set.add((modeli.s_day, modeli.channel))
    return result_list

if __name__ == '__main__':
    pass
