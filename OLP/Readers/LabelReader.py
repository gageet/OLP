# coding: -*- utf-8 -*-

import TableReader

class LabelReader:
    '''
    the Reader which can read Label
    贷款表中的标签读取器
    '''

    def __init__(self):
        pass

    def readLabel(self, tablePathList, primaryKey):
        '''
        read every element's label by primaryKey from table
        读取表中每一行的信誉度，良好或不良。
        :param tablePathList:
        :param primaryKey: the primary key's name of the table
        :return: a dict{} that contains every element's reputation
        '''
        table = LabelReader.readLabel(tablePathList)
        loanReputation = {}
        # tableElement was a dic that contains a record(row)
        for tableElement in table:
            loanReputationElement = self.getReputation(tableElement, primaryKey)
            loanReputation = dict(loanReputation, **loanReputationElement)
        return loanReputation

    def getReputation(self, tableElement, primaryKey):
        '''
        get the element's reputation
        :param tableElement:
        :param primaryKey:
        :return: a dict{} contains keyNumber(as key) and reputation(as value)
        '''
        reputation = {}
        reputation[tableElement[primaryKey]] = self.calculateReputation(tableElement)
        return reputation

    def calculateReputation(self, tableElement):
        '''
        whether this element is a bad reputation record or not. True stands bad, and False stands good.
        :param tableElement:
        :return: True or False.
        '''

        return False
