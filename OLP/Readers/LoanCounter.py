# -*- coding: utf-8 -*-

from CounterConfig import loanCountTitle, loanCustNoTitle, loanNoTitle # 该属性计算方式，客户号，贷款协议号
from ReaderTools import UniPrinter

class LoanCounter:

    def __init__(self, loanTable):
        # 原始贷款表的 索引表，贷款表，客户与协议X对应表
        self.LTTitle2index, self.LTLoans, self.cust2Proto = loanTable

    def countLoan(self):
        newLoans = {}
        title2index = self.buildIndex(loanCountTitle)
        for custom in self.cust2Proto:
            custProtoRecords = []
            for protoIndex in self.cust2Proto[custom]:
                print self.LTLoans[protoIndex]
                custProtoRecords.append(self.LTLoans[protoIndex])
            #UniPrinter().pprint(custProtoRecords)
            print custProtoRecords

            # 新建值
            newCustRecords = [custom, ]
            for titleKey in loanCountTitle:
                newCustRecords.append(self.calcNewValue(titleKey, custProtoRecords))
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

    def calcNewValue(self, titleKey, custProtoRecords):
        formula = loanCountTitle[titleKey]
        keyRecords = [x[self.LTTitle2index[titleKey]] for x in custProtoRecords]
        print keyRecords
        return formula(keyRecords)