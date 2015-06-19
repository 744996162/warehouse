__author__ = 'Administrator'

from service import hb_channel_service
from util.date_prepare import *

def hb_channel():
    yestoday = getYestoday()
    today = getToday()
    hb_channel_service.hb_channel_active_daily(yestoday, today)
    hb_channel_service.hb_channel_new_users_daily(yestoday, today)
    hb_channel_service.hb_channel_order_daily(yestoday, today)


if __name__ == "__main__":
    hb_channel()




    pass