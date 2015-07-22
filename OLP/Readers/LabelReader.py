# coding: -*- utf-8 -*-

import TableReader

class LabelReader:
    '''
    the Reader which can read Labels
    贷款表中的标签读取器
    '''

    reputation = 'reputation'

    def __init__(self):
        pass

    def readLabel(self, table):
        '''
        read every record's label by primaryKey from table
        读取表中每一行的信誉度，良好或不良。
        :param table: a table contains all the records of loan(already deleted or merged duplications)
        :return: a dict{} that contains every tableRecord's reputation
        '''
        loanReputation = {}
        # tableRecord was a dic that contains a record(row)
        for tableRecord in table:
            loanReputationRecord = self.getReputation(tableRecord)
            loanReputation = dict(loanReputation, **loanReputationRecord)
        return loanReputation

    def getReputation(self, tableRecord):
        '''
        get the record's reputation
        :param tableRecord:
        :return: a dict{} contains keyNumber(as key) and reputation(as value)
        '''
        reputation = {}
        tableRecord[reputation] = self.calculateReputation(tableRecord)
        return reputation

    def calculateReputation(self, tableRecord):
        '''
        whether this tableRecord is a bad reputation record or not. True stands bad, and False stands good.
        :param tableRecord:
        :return: True or False.
        '''
        return self.judgeRule1(tableRecord) or self.judgeRule2(tableRecord)

    def judgeRule1(tableRecord):
        pass

    def judgeRule2(tableRecord):
        pass

