# coding: utf-8

from CounterConfig import loanCustNoTitle, custNoTitle, loanNoTitle


class FeatureBuilder:
    def __init__(self, loanTable, transFeatTable, prodFeatTable):
        self.LTTitle2index, self.LTLoans = loanTable
        self.TFTTitle2index, self.TFTTrans = transFeatTable
        self.PFTTitle2index, self.PFTProds = prodFeatTable
        self.title2index = {loanNoTitle:0, custNoTitle:1}

    def buildFeature(self):
        resultRecords = []
        for exeTime,loanNo in enumerate(self.LTLoans):
            loanRecord = self.LTLoans[loanNo]
            customerNo = loanRecord[self.LTTitle2index[loanCustNoTitle]]
            transRecord = self.TFTTrans[customerNo]
            prodRecord = self.PFTProds[customerNo]
            features = self.getFeature(exeTime, loanNo, customerNo, loanRecord, transRecord, prodRecord)
            resultRecords.append([loanNo, customerNo, features])
        return self.title2index, resultRecords

    def getFeature(self, exeTime, loanNo, customerNo, loanRecord, transRecord, prodRecord):
        record = [loanNo, customerNo]
        propList = [loanCustNoTitle, custNoTitle, loanNoTitle]
        index = 2

        for loanPropKey in self.LTTitle2index:
            if loanPropKey not in propList:
                record.append(loanRecord[self.LTTitle2index[loanPropKey]])
                propList.append(loanPropKey)
                if exeTime == 0:
                    self.title2index[loanPropKey] = index
                    index += 1

        for transPropKey in self.TFTTitle2index:
            if transPropKey not in propList:
                record.append(transRecord[self.TFTTitle2index[transPropKey]])
                propList.append(transPropKey)
                if exeTime == 0:
                    self.title2index[transPropKey] = index
                    index += 1

        for prodPropKey in self.PFTTitle2index:
            if prodPropKey not in propList:
                record.append(prodRecord[self.PFTTitle2index[prodPropKey]])
                propList.append(prodPropKey)
                if exeTime == 0:
                    self.title2index[prodPropKey] = index
                    index += 1

        return record