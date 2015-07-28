# -*- coding: utf-8 -*-

from ReaderTools import TimeTools


class LabelReader:
    """
    贷款表中的标签读取器
    """

    # 注意！！！
    # 下面的类变量需要从配置文件中读取
    custNo = '核心客户号'
    debtDate = '最近欠款日期'
    statDate = '统计日期'
    lastRepayDate = '上次付款日期'
    shouldRepayDate = '本月应还款日期'
    defaultDebtDate = '0001/1/1'

    def __init__(self, loans, loansFiltered):
        self.table = loans
        self.tableFiltered = loansFiltered

    def readLabel(self):
        '''
        从贷款表中得到每一行的信誉度，良好或不良。
        :param table: 已经读取且去重的贷款协议表
        :return: [[协议号，客户号，是否不良]，[协议号，客户号，是否不良]，……]
        '''
        tableContentDict = self.table[1]
        self.title2index = self.table[0]
        loanReputation = []
        # tableKey was a dic that contains a record(row)
        for tableKey in tableContentDict:
            loanReputationRecord = self.getReputation(tableContentDict[tableKey], tableKey)
            loanReputation.append(loanReputationRecord)
        # TODO
        return loanReputation

    def getReputation(self, contentDictValue, tableKey):
        '''
        得到该条记录的信誉度，
        :param contentDictValue:
        :param tableKey:
        :return: [协议号，客户号，是否不良]
        '''
        return [tableKey, contentDictValue[self.title2index[self.custNo]][0], self.calculateReputation(contentDictValue)]

    def calculateReputation(self, contentDictValue):
        '''
        该条记录是否是不良贷款，True代表是不良贷款，False代表不是
        :param contentDictValue:
        :return: True or False.
        '''
        return self.rule1(contentDictValue)

    def rule1(self, contentDictValue):
        '''
        欠款月份是否等于统计月份，如果是，则返回true。根据每个贷款记录有多少个月份的数据，循环月份数量的次数
        :param contentDictValue:
        :return: True or False.
        '''
        for listSize in range(len(contentDictValue[1])):
            debtDate = TimeTools().str2Date(contentDictValue[self.title2index[self.debtDate]][listSize], "/")
            statDate = TimeTools().str2Date(contentDictValue[self.title2index[self.statDate]][listSize], "/")
            if debtDate.year == statDate.year and debtDate.month == statDate.month:
                return True
        return self.rule2(contentDictValue)

    def rule2(self, contentDictValue):
        '''
        最近欠款日期为默认值（贷款未结清），且未提前还款则返回true。根据每个贷款记录有多少个月份的数据，循环月份数量的次数
        :param contentDictValue:
        :return: True or False.
        '''
        for listSize in range(len(contentDictValue[1])):
            lastRepayDate = TimeTools().str2Date(contentDictValue[self.title2index[self.lastRepayDate]][listSize], "/")
            shouldRepayDate = TimeTools().str2Date(contentDictValue[self.title2index[self.shouldRepayDate]][listSize], "/")
            if lastRepayDate > shouldRepayDate and contentDictValue[self.title2index[self.debtDate]][listSize] == self.defaultDebtDate:
                return True
        return False

if __name__ == '__main__':
    from CMSBReaders import CMSBLoanReader
    from ReaderTools import UniPrinter
    import os
    loan = CMSBLoanReader([os.path.join(os.path.dirname(os.path.realpath(__file__)),'loanTablen1.txt'), os.path.join(os.path.dirname(os.path.realpath(__file__)),'loanTablen2.txt')], 'ContactNo')
    loanTable = loan.read()
    UniPrinter().pprint(loanTable)
    labelFilter = LabelReader().readLabel(loanTable,'ContactNo')
    UniPrinter().pprint(labelFilter)

