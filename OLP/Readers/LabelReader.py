# coding: -*- utf-8 -*-

from datetime import *


class LabelReader:
    """
    the Reader which can read Label
    贷款表中的标签读取器
    """

    # Notice!!!
    # the class variable will be defined by the imported config file
    debtDate = ''
    statDate = ''
    lastRepayDate = ''
    shouldRepayDate = ''
    defaultDebtDate = ''


    def __init__(self):
        pass

    def readLabel(self, table, primaryKey):
        '''
        read every record's label by primaryKey from table
        读取表中每一行的信誉度，良好或不良。
        :param table: a table contains all the records of loan(already deleted or merged duplications)
        :param primaryKey: the primary key's name of the table
        :return: a dict{} that contains every tableRecord's reputation
        '''
        loanReputation = {}
        # tableRecord was a dic that contains a record(row)
        for tableRecord in table:
            loanReputationRecord = self.getReputation(tableRecord, primaryKey)
            loanReputation = dict(loanReputation, **loanReputationRecord)
        return loanReputation

    def getReputation(self, tableRecord, primaryKey):
        '''
        get the record's reputation
        :param tableRecord:
        :param primaryKey:
        :return: a dict{} contains keyNumber(as key) and reputation(as value)
        '''
        reputation = {}
        reputation[tableRecord['primaryKey']] = self.calculateReputation(tableRecord)
        return reputation

    def calculateReputation(self, tableRecord):
        '''
        whether this tableRecord is a bad reputation record or not. True stands bad, and False stands good.
        :param tableRecord:
        :return: True or False.
        '''
        return self.rule1(tableRecord)

    def rule1(self, tableRecord):
        '''
        whether the debt date equals to stat date. If so, return True.
        :param tableRecord:
        :return:
        '''
        debtDate = tableRecord[self.debtDate]
        statDate = tableRecord[self.statDate]
        if debtDate == statDate:
            return True
        else:
            return self.rule2(self, tableRecord)

    def rule2(self, tableRecord):
        lastRepayDate = datetime.strptime(tableRecord[self.lastRepayDate], "%Y//%m//%d")
        shouldRepayDate = datetime.strptime(tableRecord[self.shouldRepayDate], "%Y//%m//%d")
        if lastRepayDate > shouldRepayDate or tableRecord[self.debtDate] == self.defaultDebtDate:
            return True
        return False
