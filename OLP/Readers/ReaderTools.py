# coding: utf-8
from datetime import datetime


class TimeTools:
    '''
    工具类，提供操作数据时的一些工具
    '''
    def __init__(self):
        pass

    def str2Date(self, str, separator):
        return datetime.strptime(str, "%Y"+separator+"%m"+separator+"%d")