# coding: utf-8

from OLP.Readers.Reader import Reader

 
class CMSBLoanReader(Reader):
    '''
    贷款数据读取类
    '''
    def __init__(self, filenames, primKey):
        self.filenames = filenames
        self.primKey = primKey

    def read(self):
        filenames = self.filenames
        nMonths = len(filenames)
        title2index = {}
        loans = {}

        # 遍历nMonth月数据
        for i, filename in enumerate(filenames):
            inFile = open(filename)

            # 读取第一行，获取字段名
            firstLine = inFile.readline()
            titles = firstLine.strip().split('\t')
            for index, title in enumerate(titles):
                title2index[title] = index

            # 读取剩余行，获取各字段对应数据
            for line in inFile:
                vals = line.strip().split('\t')
                primKeyIndex = title2index[self.primKey]
                primKeyVal = vals[primKeyIndex]
                if primKeyVal not in loans:
                    loan = []
                    for j, val in enumerate(vals):
                        loan.append([''] * nMonths)
                        loan[j][i] = val
                    loans[primKeyVal] = loan
                else:
                    loan = loans[primKeyVal]
                    for j, val in enumerate(vals):
                        loan[j][i] = val

        return title2index, loans


class CMSBTransReader(Reader):
    '''
    流水数据读取类
    '''
    def __init__(self, filenames, primKey):
        self.filenames = filenames
        self.primKey = primKey

    def read(self):
        title2index = {}
        transs = {}

        # 遍历nMonth月数据
        for i, filename in enumerate(self.filenames):
            inFile = open(filename)

            # 读取第一行，获取字段名
            firstLine = inFile.readline()
            titles = firstLine.strip().split('\t')
            for index, title in enumerate(titles):
                title2index[title] = index

            # 读取剩余行，获取各字段对应数据
            for line in inFile:
                vals = line.strip().split('\t')
                primKeyIndex = title2index[self.primKey]
                primKeyVal = vals[primKeyIndex]
                if primKeyVal not in transs:
                    trans = []
                    for val in vals:
                        trans.append([val])
                    transs[primKeyVal] = trans
                else:
                    trans = transs[primKeyVal]
                    for j, val in enumerate(vals):
                        trans[j].append(val)

        return title2index, transs


class ContactReader(Reader):
    '''
    产品签约表读取类
    签约表数据结构: Table{ CustomerId : [ [tableRecordValue1, tableRecordValue1Date], [tableRecordValue2, tableRecordValue2Date], ……]}
    '''

    # 注意！！！
    # 下面的类变量需要从配置文件中读取
    signedProdCode = 'signedProdCode'
    signedProdDate = 'signedProdDate'

    def __init__(self, filenames, primKey):
        self.filenames = filenames
        self.primKey = primKey

    def read(self):
        wholeTable = {}
        for tablePath in self.filenames:
            tableObject = open(tablePath)
            title2index = {}
            titleList = tableObject.readline().strip().split('\t')
            for index, title in enumerate(titleList):
                title2index[title] = index
            print tableObject,'abc'

            for tableRecord in tableObject:
                tableList = tableRecord.strip().split('\t')
                tableRecordKey = tableList[title2index[self.primKey]]
                tableRecordValue = tableList[title2index[self.signedProdCode]]
                tableRecordValueDate = tableList[title2index[self.signedProdDate]]

                if tableRecordKey in wholeTable:
                    wholeTable[tableRecordKey].append([tableRecordValue, tableRecordValueDate])
                else:
                    wholeTable[tableRecordKey] = [[tableRecordValue, tableRecordValueDate],]
        return wholeTable