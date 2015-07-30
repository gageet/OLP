# -*- coding: utf-8 -*-

from ReaderTools import TimeTools
import CounterConfig


class LabelReader:
    """
    贷款表中的标签读取器。调用readLabel即可
    """

    # 注意！！！
    # 下面的类变量从配置文件中读取
    custNo = CounterConfig.loanCustNoTitle
    debtDate = CounterConfig.debtDate
    statDate = CounterConfig.statDate
    lastRepayDate = CounterConfig.lastRepayDate
    shouldRepayDate = CounterConfig.shouldRepayDate
    defaultDebtDate = CounterConfig.defaultDate

    def __init__(self, loans4Labeling, loansFiltered):
        '''
        :param loans4Labeling: 需要打标签的贷款表，格式(特征索引{}, 贷款表{})
        :param loansFiltered: 用以过滤哪些需要进行打标签贷款表，格式(特征索引{}, 贷款表{})
        :return:
        '''
        self.table4Labeling = loans4Labeling
        self.tableFiltered = loansFiltered

    def readLabel(self):
        '''
        从贷款表中得到每一行的信誉度，良好或不良。
        :param table4Labeling: 已经读取且去重的贷款协议表
        :return: [[客户号，是否不良]，[客户号，是否不良]，……]
        '''
        cust2prot = self.table4Labeling[2]
        tableContentDict = self.table4Labeling[1]
        self.title2index = self.table4Labeling[0]
        loanReputations = []

        for cust in cust2prot:
            reput = 0
            for proto in cust2prot[cust]:
                if self.calculateReputation(tableContentDict[proto], proto) == 1:
                    reput = 1
                    break
            loanReputations.append([cust, reput])
        return loanReputations
        # for tableKey in tableContentDict:
        #     if tableKey in self.tableFiltered:
        #         loanReputationRecord = self.getReputation(tableContentDict[tableKey], tableKey)
        #         loanReputations.append(loanReputationRecord)
        # return loanReputations

    # def getReputation(self, contentDictValue, tableKey):
    #     '''
    #     得到该条记录的信誉度。
    #     :param contentDictValue:
    #     :param tableKey:
    #     :return: [协议号，客户号，是否不良]
    #     '''
    #     return [tableKey, contentDictValue[self.title2index[self.custNo]][0], self.calculateReputation(contentDictValue)]

    def calculateReputation(self, contentDictValue):
        '''
        该条记录是否是不良贷款，1代表是不良贷款，0代表不是
        :param contentDictValue:
        :return: 1 or 0.
        '''
        return self.rule1(contentDictValue)

    def rule1(self, contentDictValue):
        '''
        欠款月份是否等于统计月份，如果是，则返回1。根据每个贷款记录有多少个月份的数据，循环月份数量的次数
        :param contentDictValue:
        :return: 1 or 0.
        '''
        for listSize in range(len(contentDictValue[1])):
            debtDate = TimeTools().str2Date(contentDictValue[self.title2index[self.debtDate]][listSize], "/")
            statDate = TimeTools().str2Date(contentDictValue[self.title2index[self.statDate]][listSize], "/")
            if debtDate.year == statDate.year and debtDate.month == statDate.month:
                return 1
        return self.rule2(contentDictValue)

    def rule2(self, contentDictValue):
        '''
        最近欠款日期为默认值（贷款未结清），且未提前还款则返回1。根据每个贷款记录有多少个月份的数据，循环月份数量的次数
        :param contentDictValue:
        :return: True or False.
        '''
        for listSize in range(len(contentDictValue[1])):
            lastRepayDate = TimeTools().str2Date(contentDictValue[self.title2index[self.lastRepayDate]][listSize], "/")
            shouldRepayDate = TimeTools().str2Date(contentDictValue[self.title2index[self.shouldRepayDate]][listSize], "/")
            if lastRepayDate > shouldRepayDate and contentDictValue[self.title2index[self.debtDate]][listSize] == self.defaultDebtDate:
                return 1
        return 0
