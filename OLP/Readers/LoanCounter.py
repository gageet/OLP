# -*- coding: utf-8 -*-

from CounterConfig import loanCountTitle, loanCustNoTitle, loanNoTitle # 该属性计算方式，客户号，贷款协议号
from ReaderTools import UniPrinter

class LoanCounter:
    '''
    生成新的贷款表，将每一个月内，同一用户的贷款数据进行合并。调用countLoan即可
    '''
    def __init__(self, loanTable):
        # 原始贷款表的 索引表，贷款表，客户与协议X对应表
        self.LTTitle2index, self.LTLoans, self.cust2Proto = loanTable

    def countLoan(self):
        '''
        :return: 格式 特征索引表，{客户号：客户特征}，用户号协议号对应表
        '''
        # 存放新的贷款表，将每一个月内，同一用户的贷款数据进行合并
        newLoans = {}
        # 生成新贷款表的索引表
        title2index = self.buildIndex(loanCountTitle)
        # 循环得到每个用户
        for custom in self.cust2Proto:
            custProtoRecords = []
            # 循环每个用户的贷款记录
            for protoIndex in self.cust2Proto[custom]:
                custProtoRecords.append(self.LTLoans[protoIndex])

            # 存放某个用户的所有贷款
            newCustRecords = [ ]

            customs = []
            for month in range(len(custProtoRecords[0][0])):
                customs.append(custom)
            newCustRecords.append(customs)

            # 循环需要合并的贷款属性
            for titleKey in loanCountTitle:
                newCustRecords.append(self.calcNewValue(custom, titleKey, custProtoRecords))

            newLoans[custom] = newCustRecords
        return title2index, newLoans, self.cust2Proto

    def buildIndex(self, loanCountTitle):
        '''
        产生新的索引表c
        :param loanCountTitle:
        :return:
        '''
        title2index = {loanNoTitle:0}
        i = 1
        for titleKey in loanCountTitle:
            title2index[titleKey] = i
            i += 1
        return title2index

    def calcNewValue(self, custom, titleKey, custProtoRecords):
        '''
        合并该月该用户该属性的所有值。合并规则存在loanCountTitle中
        :param custom:
        :param titleKey:
        :param custProtoRecords:
        :return:
        '''
        formula = loanCountTitle[titleKey]
        result = []

        for month in range(len(custProtoRecords[0][0])):
            keyRecords = [x[self.LTTitle2index[titleKey]][month] for x in custProtoRecords]
            result.append(formula(keyRecords))
        return result