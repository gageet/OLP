# -*- coding: utf-8 -*-

from ReaderTools import TimeTools
from datetime import datetime

class ContactDateFilter():
    '''
    客户产品签约表的过滤，目前只过滤签约时间大于统计时间的
    '''

    # 注意！！！
    # 下面的类变量需要从配置文件中读取
    statDate = '2014/1/19'

    def __init__(self, statDate):
        self.statDate = statDate

    def filter(self,contactTable):
        '''
        过滤签约时间大于统计时间的记录
        :param contactTable: 传入的列表
        :return: 过滤后的记录
        '''
        delCustNo = []
        for key in contactTable:
            delProdNo = []
            for index, recordValue in enumerate(contactTable[key]):
                if not isinstance(recordValue[1], datetime):
                    recordValueDate = TimeTools().str2Date(recordValue[1], '/')
                if not isinstance(self.statDate, datetime):
                    statDate = TimeTools().str2Date(self.statDate, '/')
                # 如果记录中的签约时间大于统计时间，则将此条签约记录标记为将删除记录，加入delProdNo的列表中
                if recordValueDate > statDate:
                    delProdNo.append(index)
            # 如果只删除客户的部分记录, 则删除这些记录
            if (not len(delProdNo) == len(contactTable[key])) and (not len(delProdNo) == 0):
                self.deleteRecord(contactTable[key], delProdNo)
            # 如果删除客户的全部记录, 则标记这个客户在delCustNo列表中，在循环外删除
            elif len(delProdNo) == len(contactTable[key]):
                delCustNo.append(key)

        if not len(delCustNo) == 0:
            self.deleteRecord(contactTable,delCustNo)
        return contactTable

    def deleteRecord(self, sourceTable, delList):
        for keyOrIndex in delList:
            del sourceTable[keyOrIndex]


if __name__ == '__main__':
    from CMSBReaders import ContactReader
    import os
    tableObject = ContactReader([os.path.join(os.path.dirname(os.path.realpath(__file__)),'contactTable.txt'),], 'custNo')
    table = tableObject.read()
    print 'surceTable', table
    filter1 = ContactDateFilter('2014/3/19')
    result1 = filter1.filter(table)
    print 'resultTable', result1
    filter1 = ContactDateFilter('2013/3/19')
    result1 = filter1.filter(table)
    print 'resultTable', result1
    filter1 = ContactDateFilter('2012/3/19')
    result1 = filter1.filter(table)
    print 'resultTable', result1
    filter1 = ContactDateFilter('2011/3/19')
    result1 = filter1.filter(table)
    print 'resultTable', result1

