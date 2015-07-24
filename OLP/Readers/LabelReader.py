# -*- coding: utf-8 -*-

from datetime import *


class LabelReader:
    """
    贷款表中的标签读取器
    """

    # 注意！！！
    # 下面的类变量需要从配置文件中读取
    debtDate = 'debtDate'
    statDate = 'statDate'
    lastRepayDate = 'lastRepayDate'
    shouldRepayDate = 'shouldRepayDate'
    defaultDebtDate = 'defaultDebtDate'


    def __init__(self):
        pass

    def readLabel(self, table, primaryKey):
        '''
        读取表中每一行的信誉度，良好或不良。
        :param table: 已经读取且去重的贷款协议表
        :param primaryKey: 表的主键，一般是贷款协议号
        :return: dict{ 协议号：信誉度}
        '''
        loanReputation = {}
        # tableRecord was a dic that contains a record(row)
        for tableRecord in table:
            loanReputationRecord = self.getReputation(tableRecord, primaryKey)
            loanReputation = dict(loanReputation, **loanReputationRecord)
        return loanReputation

    def getReputation(self, tableRecord, primaryKey):
        '''
        得到该条记录的信誉度，
        :param tableRecord:
        :param primaryKey:
        :return: dict{ 协议号：信誉度}
        '''
        reputation = {}
        reputation[tableRecord[primaryKey]] = self.calculateReputation(tableRecord)
        return reputation

    def calculateReputation(self, tableRecord):
        '''
        该条记录是否是不良贷款，True代表是不良贷款，False代表不是
        :param tableRecord:
        :return: True or False.
        '''
        return self.rule1(tableRecord)

    def rule1(self, tableRecord):
        '''
        欠款月份是否等于统计月份，如果是，则返回true
        :param tableRecord:
        :return:
        ''' 
        debtDate = datetime.strptime(tableRecord[self.debtDate], "%Y/%m/%d")
        statDate = datetime.strptime(tableRecord[self.statDate], "%Y/%m/%d")
        if debtDate.year == statDate.year and debtDate.month == statDate.month:
            return True
        else:
            return self.rule2(tableRecord)

    def rule2(self, tableRecord):
        '''
        最近欠款日期为默认值（贷款未结清），且未提前还款则返回true
        :param tableRecord:
        :return:
        '''
        lastRepayDate = datetime.strptime(tableRecord[self.lastRepayDate], "%Y/%m/%d")
        shouldRepayDate = datetime.strptime(tableRecord[self.shouldRepayDate], "%Y/%m/%d")
        if lastRepayDate > shouldRepayDate and tableRecord[self.debtDate] == self.defaultDebtDate:
            return True
        return False

if __name__ == '__main__':
    list = [{'debtDate':'2000/1/1', 'statDate':'2000/1/9', 'lastRepayDate':'2000/1/1', 'shouldRepayDate':'2000/1/1', 'defaultDebtDate':'0001/1/1', 'pk':'lgj'}]
    labelReader = LabelReader()
    dic = labelReader.readLabel(list,'pk')
    print dic