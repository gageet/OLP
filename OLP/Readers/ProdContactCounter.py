# -*- coding: utf-8 -*-

from ReaderTools import TimeTools
from datetime import datetime
from CounterConfig import prodContactDateTitle, defaultDate
from CounterConfig import custNoTitle, prodContactCodeTitle, contactAmountTitle

class ProdContactCounter:
    '''
    根据产品签约表，生成产品签约特征表。调用countProdContact即可
    '''
    def __init__(self, contactTableTuple, statDate):
        '''
        根据产品签约表，生成产品签约特征表
        :param contactTableTuple: 格式(特征索引{}, 产品签约表{})
        :param statDate: 统计日期
        '''
        self.countTitle2Index, self.contactTable = ContactDateFilter(contactTableTuple, statDate).filter()

    def countProdContact(self):
        '''
        生成产品签约特征表。格式 产品签约特征表{客户号：签约数量}
        '''
        resultTable = {}
        for key in self.contactTable:
            value = self.count(self.contactTable[key])
            resultTable[key] = value
        #resultTitle2Index = {custNoTitle:'0', contactAmountTitle:'1'}
        return resultTable

    def count(self,contactRecords):
        '''
        计算某个客户的特征（签约数量）
        :param contactRecords: 该客户的所有签约内容
        :return: 签约数量
        '''
        tempList = []
        record = contactRecords[self.countTitle2Index[prodContactCodeTitle]]
        countNum = 0
        for index in record:
            # 过滤重复签约
            if not index in tempList:
                tempList.append(index)
                countNum += 1

        return countNum

class ContactDateFilter():
    '''
    客户产品签约表的过滤，目前只过滤签约时间大于统计时间的
    '''
    statDate = defaultDate

    def __init__(self, contactTableTuple, statDate):
        self.statDate = statDate
        self.countTitle2Index, self.contactTable = contactTableTuple

    def filter(self):
        '''
        过滤签约时间大于统计时间的记录
        :param self.contactTable: 传入的列表
        :return: 过滤后的记录
        '''

        delCustNo = []
        for key in self.contactTable:
            delProdNo = []

            for index in range(len(self.contactTable[key][0])):

                if not isinstance(self.contactTable[key][self.countTitle2Index[prodContactDateTitle]][index], datetime):
                    recordValueDate = TimeTools().str2Date(self.contactTable[key][self.countTitle2Index[prodContactDateTitle]][index], '/')
                if not isinstance(self.statDate, datetime):
                    statDate = TimeTools().str2Date(self.statDate, '/')
                # 如果记录中的签约时间大于统计时间，则将此条签约记录标记为将删除记录，加入delProdNo的列表中
                if recordValueDate > statDate:
                    delProdNo.append(index)

            # 如果只删除客户的部分记录, 则删除这些记录
            if (not len(delProdNo) == len(self.contactTable[key][0])) and (not len(delProdNo) == 0):
                self.deleteRecord(self.contactTable[key], delProdNo)
            # 如果删除客户的全部记录, 则标记这个客户在delCustNo列表中，在循环外删除
            elif len(delProdNo) == len(self.contactTable[key][0]):
                delCustNo.append(key)

        if not len(delCustNo) == 0:
            self.deleteCust(self.contactTable,delCustNo)
        return self.countTitle2Index, self.contactTable

    def deleteRecord(self, sourceTable, delList):

        delList.reverse()
        sourceTableLength = range(len(sourceTable))

        for recordNo in delList:
            for propNo in sourceTableLength:
                del sourceTable[propNo][recordNo]

    def deleteCust(self, sourceTable, delCust):
        for key in delCust:
            del sourceTable[key]