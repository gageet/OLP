# coding: utf-8

from CounterConfig import loanCustNoTitle, custNoTitle, loanNoTitle, contactAmountTitle
from CounterConfig import loanFeatTitle


class FeatureBuilder:
    '''
    根据输入的各个表的特征，合成成一张特征表。在建立该类对象后，利用buildFeature方法获取。
    '''
    def __init__(self, loanTable, transFeatTable, prodFeatTable):
        '''
        :param loanTable: 贷款表的特征。格式 (特征表索引{特征名：该特征索引}, 贷款表特征{})
        :param transFeatTable: 交易流水特征表的特征。格式 (特征表索引{特征名：该特征索引}, 交易流水表特征{})
        :param prodFeatTable: 产品签约特征表的特征。格式 {用户号: 用户签约数量}
        '''
        self.LTTitle2index, self.LTLoans, self.cust2Proto = loanTable
        self.TFTTitle2index, self.TFTTrans = transFeatTable
        self.prodFeatTable = prodFeatTable
        self.title2index = {}

    def buildFeature(self):
        '''
        为每个协议号返回特征表。格式(特征表索引{特征名：该特征索引},[[贷款协议号，客户号，[特征1，特征2，...]]，[贷款协议号，客户号，[特征1，特征2，...]], ...])
        :return:
        '''
        resultRecords = []
        for exeTime,custNo in enumerate(self.LTLoans):
            loanRecord = self.LTLoans[custNo]
            transRecord = self.TFTTrans[custNo]
            prodRecord = self.prodFeatTable[custNo]
            # 计算该贷款的所有特征并返回
            features = self.getFeature(exeTime, custNo, loanRecord, transRecord, prodRecord)
            resultRecords.append([custNo, features])
        return self.title2index, resultRecords

    def getFeature(self, exeTime, customerNo, loanRecord, transRecord, prodRecord):
        '''
        计算某个协议号的特征
        :param exeTime: 第几次调用本函数
        :param customerNo: 用户号
        :param loanRecord: 贷款表
        :param transRecord: 交易流水特征表
        :param prodRecord: 产品签约特征表
        :return: 该协议号的所有特征
        '''
        record = []
        # 记录加入了哪些特征title，用以避免添加重复特征
        propList = [loanCustNoTitle, custNoTitle, loanNoTitle]
        # 特征在list中的索引值
        index = 0
        # 提取了几个月的数据
        months = range(len(loanRecord[0]))

        # 加入贷款表中的特征
        for loanPropKey in self.LTTitle2index:
            if loanPropKey not in propList and loanFeatTitle.has_key(loanPropKey):
                for month in months:
                    record.append(loanRecord[self.LTTitle2index[loanPropKey]][month])
                    propList.append(loanPropKey)
                    #如果第一次执行该函数，则将该特征的索引加入“特征表索引”
                    if exeTime == 0:
                        self.title2index[loanPropKey + str(month)] = index
                        index += 1
        # 加入交易流水特征表中的特征
        for transPropKey in self.TFTTitle2index:
            if transPropKey not in propList:
                record.append(transRecord[self.TFTTitle2index[transPropKey]])
                propList.append(transPropKey)
                if exeTime == 0:
                    self.title2index[transPropKey] = index
                    index += 1

        # 加入产品签约特征表中的特征
        record.append(prodRecord)
        propList.append(contactAmountTitle)
        if exeTime == 0:
            self.title2index[contactAmountTitle] = index
            index += 1

        return record