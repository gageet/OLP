# -*- coding: utf-8 -*-

import os
from OLP.Readers.Reader import Reader


class CMSBFieldConvertor(object):

    def __init__(self, fieldName2fieldType):
        self.fieldName2fieldType = fieldName2fieldType

    def buildIndex(self, fieldName2index):
        fieldNameRsrvd2index = {}
        for fieldName in fieldName2index:
            if fieldName in self.fieldName2fieldType:  # 保留目标字段
                fieldNameRsrvd2index[fieldName] = len(fieldNameRsrvd2index)
        self.fieldName2index = dict(fieldName2index)
        self.fieldNameRsrvd2index = dict(fieldNameRsrvd2index)
        return fieldNameRsrvd2index

    def convert(self, fields):
        fieldsCnvtd = [0.0] * len(self.fieldNameRsrvd2index)
        for fieldName in self.fieldNameRsrvd2index:
            type_ = self.fieldName2fieldType[fieldName]
            indexOld = self.fieldName2index[fieldName]
            indexNew = self.fieldNameRsrvd2index[fieldName]
            fieldsCnvtd[indexNew] = type_(fields[indexOld])
        return fieldsCnvtd


#class CMSBFieldFilter(FieldFilter):
#    '''
#    过滤无用字段
#    '''
#    def __init__(self, fieldName2fieldType):
#        self.fieldNamesRsrvd = fieldNamesRsrvd
#        self.fieldName2index = None
#        self.fieldNameRsrvd2index = None
#
#    def buildIndex(self, fieldName2index):
#        for fieldName in fieldName2index:
#            if fieldName in self.fieldNamesRsrvd: # 保留目标字段
#                self.fieldNameRsrvd2index[fieldName] = len(self.fieldNameRsrvd2index)
#        self.fieldName2index = fieldName2index
#        return dict(self.fieldNameRsrvd2index)
#
#    def filter(self, fields):
#        '''
#        @param  fields            [field1, field2, ...]
#        @return fieldsFiltered    [fieldi1, fieldi2, ...]
#        '''
#        fieldsFiltered = [None] * len(self.fieldNameRsrvd2index)
#        for fieldName in self.fieldNameRsrvd2index:
#            indexOld = self.fieldName2index[fieldName]
#            indexNew = self.fieldNameRsrvd2index[fieldName]
#            fieldsFiltered[indexNew] = fields[indexOld]
#        return fieldsFiltered
#
#
#class CMSBFieldConvertor(FieldConvertor):
#
#    def __init__(self, fieldName2index, fieldName2fieldType):
#        self.fieldName2index = fieldName2index
#        self.fieldName2fieldType = fieldName2fieldType
#
#    def convert(self, fields):
#        for fieldName, index in self.fieldName2index.items():
#            type_ = self.fieldName2fieldType[fieldName]
#            index = self.fieldName2index[fieldName]
#            fields[index] = type_(fields[index])
#        return fields


class CMSBReader(Reader):

    def __init__(self, targets, months, loanDir, transDir, prodDir, fieldName2fieldType):
        '''
        @param targets     list, [[protolNo1, custNum1, label1], [protolNo2, custNum2, label2], ...]
        @param months      list, [month1, month2, ...]
        @param loanDir
        @param transDir
        @param fields      set, {field1, field2, ...}
        @param prodDir
        '''
        self.targets = targets
        self.months = months
        self.loanDir = loanDir
        self.transDir = transDir
        self.prodDir = prodDir
        self.fieldConvertor = CMSBFieldConvertor(fieldName2fieldType)

    def read(self):
        self.readLoans(self.targets, self.loanDir, self.months)

    def readLoans(self, targets, loanDir, months):
        fieldName2index = {}

        for i, month in enumerate(months):
            filename = os.path.join(loanDir, month)
            inFile = open(filename)

            # 读取第一行
            firstLine = inFile.readline()
            if i == 0:  # 第一次读取，利用第一行获取所有字段
                fieldNames = firstLine.strip().split('\t')
                for fieldName in fieldNames:
                    fieldName2index[fieldName] = len(fieldName2index)  # 构建原始字段索引
                fieldName2index = self.fieldConvertor.buildIndex(fieldName2index)  # 构建过滤后字段索引

            # 读取剩余行，获取各字段对应数据
            for line in inFile:
                fields = line.strip().split('\t')
                fields = self.fieldConvertor.convert(fields)
                for fieldName, index in fieldName2index.items():
                    print fieldName, fields[index], ' | ',
                print ''
                #protolNumIndex = field2index[self.enTitle2cnTitle['protolNum']]
                #protolNum = fields[protolNumIndex]
                #if protolNum in protolNums: # 属于待预测贷款
                #    if protolNum not in loans:
                #        loan = []
                #        for j, field in enumerate(fields):
                #            loan.append([''] * nMonths)
                #            loan[j][i] = field
                #        loans[primKeyVal] = loan
                #    else:
                #        loan = loans[primKeyVal]
                #        for j, field in enumerate(fields):
                #            loan[j][i] = field
            inFile.close()

        #return field2index, loans

    def readTranss(self, transDir, months):
        pass

    def readProds(self, prodDir, months):
        pass

    def merge(self, loans, transs, prods):
        pass
 
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
        field2index = {}
        loans = {}

        # 遍历nMonth月数据
        for i, filename in enumerate(filenames):
            inFile = open(filename)

            # 读取第一行，获取字段名
            firstLine = inFile.readline()
            fields = firstLine.strip().split('\t')
            for index, field in enumerate(fields):
                field2index[field] = index

            # 读取剩余行，获取各字段对应数据
            for line in inFile:
                fields = line.strip().split('\t')
                primKeyIndex = field2index[self.primKey]
                primKeyVal = fields[primKeyIndex]
                if primKeyVal not in loans:
                    loan = []
                    for j, field in enumerate(fields):
                        loan.append([''] * nMonths)
                        loan[j][i] = field
                    loans[primKeyVal] = loan
                else:
                    loan = loans[primKeyVal]
                    for j, field in enumerate(fields):
                        loan[j][i] = field

        return field2index, loans


class CMSBTransReader(Reader):
    '''
    流水数据读取类
    '''
    def __init__(self, filenames, primKey):
        self.filenames = filenames
        self.primKey = primKey

    def read(self):
        field2index = {}
        transs = {}

        # 遍历nMonth月数据
        for i, filename in enumerate(self.filenames):
            inFile = open(filename)

            # 读取第一行，获取字段名
            firstLine = inFile.readline()
            fields = firstLine.strip().split('\t')
            for index, field in enumerate(fields):
                field2index[field] = index

            # 读取剩余行，获取各字段对应数据
            for line in inFile:
                fields = line.strip().split('\t')
                primKeyIndex = field2index[self.primKey]
                primKeyVal = fields[primKeyIndex]
                if primKeyVal not in transs:
                    trans = []
                    for field in fields:
                        trans.append([field])
                    transs[primKeyVal] = trans
                else:
                    trans = transs[primKeyVal]
                    for j, field in enumerate(fields):
                        trans[j].append(field)

        return field2index, transs


class ContactReader(Reader):
    '''
    产品签约表读取类
    '''

    # 注意！！！
    # 下面的类变量需要从配置文件中读取
    signedProdCode = 'signedProdCode'
    signedProdDate = 'signedProdDate'

    def __init__(self, filenames, primKey):
        self.filenames = filenames
        self.primKey = primKey

    def read(self):
        '''
        读取产品签约表
        :return: Table{ CustomerId : [ [tableRecordValue1, tableRecordValue1Date], [tableRecordValue2, tableRecordValue2Date], ……]}
        '''
        wholeTable = {}
        for tablePath in self.filenames:
            tableObject = open(tablePath)
            field2index = {}
            fieldList = tableObject.readline().strip().split('\t')
            for index, field in enumerate(fieldList):
                field2index[field] = index
            print tableObject,'abc'

            for tableRecord in tableObject:
                tableList = tableRecord.strip().split('\t')
                tableRecordKey = tableList[field2index[self.primKey]]
                tableRecordValue = tableList[field2index[self.signedProdCode]]
                tableRecordValueDate = tableList[field2index[self.signedProdDate]]

                if tableRecordKey in wholeTable:
                    wholeTable[tableRecordKey].append([tableRecordValue, tableRecordValueDate])
                else:
                    wholeTable[tableRecordKey] = [[tableRecordValue, tableRecordValueDate],]
        return wholeTable
