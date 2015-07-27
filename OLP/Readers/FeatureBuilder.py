# coding: utf-8

from CounterConfig import loanCustNoTitle, custNoTitle, loanNoTitle, contactAmountTitle


class FeatureBuilder:
    def __init__(self, loanTable, transFeatTable, prodFeatTable):
        self.LTTitle2index, self.LTLoans = loanTable
        self.TFTTitle2index, self.TFTTrans = transFeatTable
        self.prodFeatTable = prodFeatTable
        self.title2index = {}

    def buildFeature(self):
        resultRecords = []
        for exeTime,loanNo in enumerate(self.LTLoans):
            loanRecord = self.LTLoans[loanNo]
            customerNo = loanRecord[self.LTTitle2index[loanCustNoTitle]][0]
            transRecord = self.TFTTrans[customerNo]
            prodRecord = self.prodFeatTable[customerNo]
            features = self.getFeature(exeTime, loanNo, customerNo, loanRecord, transRecord, prodRecord)
            resultRecords.append([loanNo, customerNo, features])
        return self.title2index, resultRecords

    def getFeature(self, exeTime, loanNo, customerNo, loanRecord, transRecord, prodRecord):
        record = []
        propList = [loanCustNoTitle, custNoTitle, loanNoTitle]
        index = 0
        months = range(len(loanRecord[0]))

        for loanPropKey in self.LTTitle2index:
            if loanPropKey not in propList:
                for month in months:
                    record.append(loanRecord[self.LTTitle2index[loanPropKey]][month])
                    propList.append(loanPropKey)
                    if exeTime == 0:
                        for times in months:
                            self.title2index[loanPropKey + str(times)] = index
                            index += 1

        for transPropKey in self.TFTTitle2index:
            if transPropKey not in propList:
                record.append(transRecord[self.TFTTitle2index[transPropKey]])
                propList.append(transPropKey)
                if exeTime == 0:
                    self.title2index[transPropKey] = index
                    index += 1


        record.append(prodRecord)
        propList.append(contactAmountTitle)
        if exeTime == 0:
            self.title2index[contactAmountTitle] = index
            index += 1

        return record