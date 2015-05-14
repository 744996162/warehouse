__author__ = 'Administrator'

class OrderedDict(dict):
    def __init__(self, *args, **kwargs):
        if len(args)>1:
            raise TypeError("exce")