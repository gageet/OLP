# coding: utf-8
from datetime import datetime
import pprint, cStringIO


class TimeTools:
    '''
    工具类，提供操作数据时的一些工具
    '''
    def __init__(self):
        pass

    def str2Date(self, str, separator):
        return datetime.strptime(str, "%Y"+separator+"%m"+separator+"%d")


class UniPrinter(pprint.PrettyPrinter):
    '''
    工具类，打印字典，列表或几个容器嵌套且包含中文的情况。调用格式：UniPrinter().pprint(Object)
    '''
    def format(self, obj, context, maxlevels, level):
        if isinstance(obj, unicode):
            out = cStringIO.StringIO()
            out.write('u"')
            for c in obj:
                if ord(c)<32 or c in u'"\\':
                    out.write('\\x%.2x' % ord(c))
                else:
                    out.write(c.encode("utf-8"))

            out.write('"')
            # result, readable, recursive
            return out.getvalue(), True, False
        elif isinstance(obj, str):
            out = cStringIO.StringIO()
            out.write('"')
            for c in obj:
                if ord(c)<32 or c in '"\\':
                    out.write('\\x%.2x' % ord(c))
                else:
                    out.write(c)

            out.write('"')
            # result, readable, recursive
            return out.getvalue(), True, False
        else:
            return pprint.PrettyPrinter.format(self, obj, context, maxlevels, level)
