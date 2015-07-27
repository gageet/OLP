# -*- coding: utf-8 -*-

from ReaderTools import TimeTools
from datetime import datetime

class ContactDateFilter():
    '''
    客户产品签约表的过滤，目前只过滤签约时间大于统计时间的
    '''

    # 注意！！！
    # 下面的类变量需要从配置文件中读取
    from CountConfig import prodContactDate,defaultDate
    statDate = defaultDate

    def __init__(self, statDate):
        self.statDate = statDate

    def filter(self,contactTableDic):
        '''
        过滤签约时间大于统计时间的记录
        :param contactTable: 传入的列表
        :return: 过滤后的记录
        '''
        contTitle2Index, contactTable = contactTableDic

        delCustNo = []
        for key in contactTable:
            delProdNo = []

            for index in range(len(contactTable[key][0])):

                if not isinstance(contactTable[key][contTitle2Index[self.prodContactDate]][index], datetime):
                    recordValueDate = TimeTools().str2Date(contactTable[key][contTitle2Index[self.prodContactDate]][index], '/')
                if not isinstance(self.statDate, datetime):
                    statDate = TimeTools().str2Date(self.statDate, '/')
                # 如果记录中的签约时间大于统计时间，则将此条签约记录标记为将删除记录，加入delProdNo的列表中
                if recordValueDate > statDate:
                    delProdNo.append(index)

            # 如果只删除客户的部分记录, 则删除这些记录
            if (not len(delProdNo) == len(contactTable[key][0])) and (not len(delProdNo) == 0):
                print 'OLD'
                UniPrinter().pprint(contactTable[key])
                self.deleteRecord(contactTable[key], delProdNo)
                print 'NEW'
                UniPrinter().pprint(contactTable[key])
            # 如果删除客户的全部记录, 则标记这个客户在delCustNo列表中，在循环外删除
            elif len(delProdNo) == len(contactTable[key][0]):
                delCustNo.append(key)

        if not len(delCustNo) == 0:
            self.deleteCust(contactTable,delCustNo)
        return contTitle2Index, contactTable

    def deleteRecord(self, sourceTable, delList):

        delList.reverse()
        sourceTableLength = range(len(sourceTable))

        for recordNo in delList:
            for propNo in sourceTableLength:
                del sourceTable[propNo][recordNo]

    def deleteCust(self, sourceTable, delCust):
        for key in delCust:
            del sourceTable[key]




if __name__ == '__main__':

    from CMSBReaders import CMSBReader
    import config
    from ReaderTools import UniPrinter

    tableObject = CMSBReader(config.fieldName2fieldType)
    table = tableObject.readProds(['prods.txt',])
    UniPrinter().pprint(table)
    tableFiltered = ContactDateFilter('2014/1/19').filter(table)
    UniPrinter().pprint(tableFiltered)








