# -*- coding: utf-8 -*-

import os
from OLP.Readers.Reader import Reader


class CMSBFieldProcessor(object):

    def __init__(self, fieldName2fieldType):
        self.fieldName2fieldType = fieldName2fieldType
        self.loanFieldName2IndexOld = {}
        self.loanFieldName2IndexNew = {}
        self.transFieldName2IndexOld = {}
        self.transFieldName2IndexNew = {}
        self.prodFieldName2IndexOld = {}
        self.prodFieldName2IndexNew = {}

    def buildLoanFieldNameIndex(self, fieldNames):
        return self.buildIndex(fieldNames, self.loanFieldName2IndexOld, self.loanFieldName2IndexNew)

    def buildTransFieldNameIndex(self, fieldNames):
        return self.buildIndex(fieldNames, self.transFieldName2IndexOld, self.transFieldName2IndexNew)

    def buildProdFieldNameIndex(self, fieldNames):
        return self.buildIndex(fieldNames, self.prodFieldName2IndexOld, self.prodFieldName2IndexNew)

    def buildIndex(self, fieldNames, fieldName2IndexOld, fieldName2IndexNew):
        for fieldName in fieldNames:
            fieldName2IndexOld[fieldName] = len(fieldName2IndexOld)
            if fieldName in self.fieldName2fieldType:  # 保留目标字段
                fieldName2IndexNew[fieldName] = len(fieldName2IndexNew)
        return fieldName2IndexNew

    def convertLoanFields(self, fields):
        return self.convert(fields, self.loanFieldName2IndexOld, self.loanFieldName2IndexNew)

    def convertTransFields(self, fields):
        return self.convert(fields, self.transFieldName2IndexOld, self.transFieldName2IndexNew)

    def convertProdFields(self, fields):
        return self.convert(fields, self.prodFieldName2IndexOld, self.prodFieldName2IndexNew)

    def convert(self, fields, fieldName2IndexOld, fieldName2IndexNew):
        fieldsCnvtd = [0.0] * len(fieldName2IndexNew)
        for fieldName in fieldName2IndexNew:
            type_ = self.fieldName2fieldType[fieldName]
            indexOld = fieldName2IndexOld[fieldName]
            indexNew = fieldName2IndexNew[fieldName]
            fieldsCnvtd[indexNew] = type_(fields[indexOld])
        return fieldsCnvtd

    def addLoanFields(self, fields, samples, primFieldName, fieldsRsrvd):
        self.addFields(fields, samples, primFieldName, fieldsRsrvd, self.loanFieldName2IndexNew)

    def addTransFields(self, fields, samples, primFieldName, fieldsRsrvd):
        self.addFields(fields, samples, primFieldName, fieldsRsrvd, self.transFieldName2IndexNew)

    def addProdFields(self, fields, samples, primFieldName, fieldsRsrvd):
        self.addFields(fields, samples, primFieldName, fieldsRsrvd, self.prodFieldName2IndexNew)

    def addFields(self, fields, samples, primFieldName, fieldsRsrvd, fieldName2Index):
        primFieldIndex = fieldName2Index[primFieldName]
        primField = fields[primFieldIndex]
        if primField in fieldsRsrvd:  # 属于待预测贷款
            if primField not in samples:
                sample = []
                for j, field in enumerate(fields):
                    sample.append([])
                    sample[j].append(field)
                samples[primField] = sample
            else:
                sample = samples[primField]
                for j, field in enumerate(fields):
                    sample[j].append(field)


class CMSBReader(Reader):

    def __init__(self, targets, months, loanDir, transDir, prodDir, fieldName2fieldType):
        self.targets = targets
        self.months = months
        self.loanDir = loanDir
        self.transDir = transDir
        self.prodDir = prodDir
        self.fieldProcessor = CMSBFieldProcessor(fieldName2fieldType)
        self.protolNumName = '协议号'
        self.custNumName = '我行客户号'

    def read(self):
        loanFieldName2Index, loans = self.readLoans(self.targets, self.loanDir, self.months)
        for loan in loans.values():
            for name, index in loanFieldName2Index.items():
                print '%s:%s' % (name, str(loan[index])),
            print '\n', '-' * 20
        transFieldName2Index, transs = self.readTranss(self.targets, self.transDir, self.months)
        for trans in transs.values():
            for name, index in transFieldName2Index.items():
                print '%s:%s' % (name, str(trans[index])),
            print '\n', '-' * 20
        prodFieldName2Index, prods = self.readProds(self.targets, self.prodDir, self.months)
        for prod in prods.values():
            for name, index in prodFieldName2Index.items():
                print '%s:%s' % (name, str(prod[index])),
            print '\n', '-' * 20

        return [loanFieldName2Index, loans], [transFieldName2Index, transs], [prodFieldName2Index, prods]

    def readLoans(self, targets, loanDir, months):
        protolNums = set([target[0] for target in targets])
        fieldName2Index = {}
        loans = {}

        for i, month in enumerate(months):
            filename = os.path.join(loanDir, month)
            inFile = open(filename)

            # 读取第一行
            firstLine = inFile.readline()
            if i == 0:  # 第一次读取，利用第一行获取所有字段
                fieldNames = firstLine.strip().split('\t')
                fieldName2Index = self.fieldProcessor.buildLoanFieldNameIndex(fieldNames)  # 构建字段索引

            # 读取剩余行，获取各字段对应数据
            for line in inFile:
                fields = line.strip().split('\t')
                fields = self.fieldProcessor.convertLoanFields(fields)
                self.fieldProcessor.addLoanFields(fields, loans, self.protolNumName, protolNums)
            inFile.close()

        return fieldName2Index, loans

    def readTranss(self, targets, transDir, months):
        custNums = set([target[1] for target in targets])
        fieldName2Index = {}
        transs = {}

        for i, month in enumerate(months):
            filename = os.path.join(transDir, month)
            inFile = open(filename)

            # 读取第一行
            firstLine = inFile.readline()
            if i == 0:  # 第一次读取，利用第一行获取所有字段
                fieldNames = firstLine.strip().split('\t')
                fieldName2Index = self.fieldProcessor.buildTransFieldNameIndex(fieldNames)  # 构建字段索引

            # 读取剩余行，获取各字段对应数据
            for line in inFile:
                fields = line.strip().split('\t')
                fields = self.fieldProcessor.convertTransFields(fields)
                self.fieldProcessor.addTransFields(fields, transs, self.custNumName, custNums)
            inFile.close()

        return fieldName2Index, transs

    def readProds(self, targets, prodDir, months):
        custNums = set([target[1] for target in targets])
        fieldName2Index = {}
        prods = {}

        for i, month in enumerate(months):
            filename = os.path.join(prodDir, month)
            inFile = open(filename)

            # 读取第一行
            firstLine = inFile.readline()
            if i == 0:  # 第一次读取，利用第一行获取所有字段
                fieldNames = firstLine.strip().split('\t')
                fieldName2Index = self.fieldProcessor.buildProdFieldNameIndex(fieldNames)  # 构建字段索引

            # 读取剩余行，获取各字段对应数据
            for line in inFile:
                fields = line.strip().split('\t')
                fields = self.fieldProcessor.convertProdFields(fields)
                self.fieldProcessor.addProdFields(fields, prods, self.custNumName, custNums)
            inFile.close()

        return fieldName2Index, prods

    def merge(self, loans, transs, prods):
        pass
