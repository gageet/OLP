# -*- coding: utf-8 -*-


class CMSBFieldProcessor(object):
    '''
    该类用于辅助处理表数据
    '''
    def __init__(self, fieldName2fieldType):
        self.fieldName2fieldType = fieldName2fieldType  # 字段类型
        self.loanFieldName2IndexOld = {}  # 贷款协议表原始字段索引
        self.loanFieldName2IndexNew = {}  # 贷款协议表保留字段索引
        self.transFieldName2IndexOld = {}  # 交易流水表原始字段索引
        self.transFieldName2IndexNew = {}  # 交易流水表保留字段索引
        self.prodFieldName2IndexOld = {}  # 产品签约表原始字段索引
        self.prodFieldName2IndexNew = {}  # 产品签约表保留字段索引

    def buildLoanFieldNameIndex(self, fieldNames):
        '''
        构建贷款协议表字段索引

        Args:
            fieldNames (list): 字段名列表

        Returns:
            dict: 字段索引
        '''
        return self.buildIndex(fieldNames, self.loanFieldName2IndexOld, self.loanFieldName2IndexNew)

    def buildTransFieldNameIndex(self, fieldNames):
        '''
        构建交易流水表字段索引

        Args:
            fieldNames (list): 字段名列表

        Returns:
            dict: 字段索引
        '''
        return self.buildIndex(fieldNames, self.transFieldName2IndexOld, self.transFieldName2IndexNew)

    def buildProdFieldNameIndex(self, fieldNames):
        '''
        构建产品签约表字段索引

        Args:
            fieldNames (list): 字段名列表

        Returns:
            dict: 字段索引
        '''
        return self.buildIndex(fieldNames, self.prodFieldName2IndexOld, self.prodFieldName2IndexNew)

    def buildIndex(self, fieldNames, fieldName2IndexOld, fieldName2IndexNew):
        '''
        构建字段索引

        Args:
            fieldNames (list): 字段名列表
            fieldName2IndexOld (dict): 原始字段索引
            fieldName2IndexNew (dict): 保留字段索引

        Returns:
            dict: 保留字段索引
        '''
        fieldName2IndexOld.clear()
        fieldName2IndexNew.clear()
        for fieldName in fieldNames:
            fieldName2IndexOld[fieldName] = len(fieldName2IndexOld)
            if fieldName in self.fieldName2fieldType:  # 保留目标字段
                fieldName2IndexNew[fieldName] = len(fieldName2IndexNew)
        return fieldName2IndexNew

    def convertLoanFields(self, fields):
        '''
        转换贷款协议表字段列表：过滤掉非保留字段，并将保留字段按照保留字段索引的顺序排列

        Args:
            field (list): 字段列表

        Returns:
            list: 转换后字段列表
        '''
        return self.convert(fields, self.loanFieldName2IndexOld, self.loanFieldName2IndexNew)

    def convertTransFields(self, fields):
        '''
        转换交易流水表字段列表：过滤掉非保留字段，并将保留字段按照保留字段索引的顺序排列

        Args:
            field (list): 字段列表

        Returns:
            list: 转换后字段列表
        '''
        return self.convert(fields, self.transFieldName2IndexOld, self.transFieldName2IndexNew)

    def convertProdFields(self, fields):
        '''
        转换产品签约表字段列表：过滤掉非保留字段，并将保留字段按照保留字段索引的顺序排列

        Args:
            field (list): 字段列表

        Returns:
            list: 转换后字段列表
        '''
        return self.convert(fields, self.prodFieldName2IndexOld, self.prodFieldName2IndexNew)

    def convert(self, fields, fieldName2IndexOld, fieldName2IndexNew):
        '''
        转换字段列表：过滤掉非保留字段，并将保留字段按照保留字段索引的顺序排列

        Args:
            field (list): 字段列表
            fieldName2IndexOld (dict): 原始字段索引
            fieldName2IndexNew (dict): 保留字段索引

        Returns:
            list: 转换后字段列表
        '''
        fieldsCnvtd = [0.0] * len(fieldName2IndexNew)
        for fieldName in fieldName2IndexNew:
            type_ = self.fieldName2fieldType[fieldName]
            indexOld = fieldName2IndexOld[fieldName]
            indexNew = fieldName2IndexNew[fieldName]
            fieldsCnvtd[indexNew] = type_(fields[indexOld])
        return fieldsCnvtd

    def addLoanFields(self, fields, samples, primFieldName):
        '''
        添加一项新记录(字段列表)到贷款协议表数据中

        Args:
            field (list): 字段列表
            samples (dict): 贷款协议表数据
            primFieldName (str): 主字段名
        '''
        self.addFields(fields, samples, primFieldName, self.loanFieldName2IndexNew)

    def addTransFields(self, fields, samples, primFieldName):
        '''
        添加一项新记录(字段列表)到交易流水表数据中

        Args:
            field (list): 字段列表
            samples (dict): 贷款协议表数据
            primFieldName (str): 主字段名
        '''
        self.addFields(fields, samples, primFieldName, self.transFieldName2IndexNew)

    def addProdFields(self, fields, samples, primFieldName):
        '''
        添加一项新记录(字段列表)到产品签约表数据中

        Args:
            field (list): 字段列表
            samples (dict): 贷款协议表数据
            primFieldName (str): 主字段名
        '''
        self.addFields(fields, samples, primFieldName, self.prodFieldName2IndexNew)

    def addFields(self, fields, samples, primFieldName, fieldName2Index):
        '''
        添加一项新记录(字段列表)到对应的表数据中

        Args:
            field (list): 字段列表
            samples (dict): 表数据
            primFieldName (str): 主字段名
        '''
        primFieldIndex = fieldName2Index[primFieldName]
        primField = fields[primFieldIndex]

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

    def expandSamples(self, samples, primFieldName, fieldName2Index):
        '''
        对表数据中字段的维数进行扩展,使表中所有样本的对应字段维数相同

        Args:
            samples (dict): 表数据
            primFieldName (str): 主字段名
            fieldName2Index (dict): 字段索引
        '''
        dimMax = 0
        for sample in samples.itervalues():
            for field in sample:
                dimMax = max(dimMax, len(field))
        for sample in samples.itervalues():
            for fieldName, fieldIndex in fieldName2Index.iteritems():
                field = sample[fieldIndex]
                if len(field) < dimMax:
                    type_ = self.fieldName2fieldType[fieldName]
                    sample[fieldIndex] = [type_()] * (dimMax - len(field))
                    sample[fieldIndex].extend(field)
        return samples


class CMSBReader(object):
    '''
    该类用于读取若干月(比如n ~ n+m-1共m个月)贷款协议表，交易流水表和产品签约表的数据。

    贷款协议表数据保存格式为：
    {贷款协议号1: [[字段1第n月数据, 字段1第n+1月数据, ..., 字段1第n+m-1月数据],
                   [字段2第n月数据, 字段2第n+1月数据, ..., 字段2第n+m-1月数据],
                   ...
                  ],
     贷款协议号2: [[字段1第n月数据, 字段1第n+1月数据, ..., 字段1第n+m-1月数据],
                   [字段2第n月数据, 字段2第n+1月数据, ..., 字段2第n+m-1月数据],
                   ...
                  ],
     ...,
    }

    交易流水表数据保存格式为(假定用户i在n ~ n+m-1月内共有pi笔交易)：
    {客户号1: [[字段1第1笔数据, 字段1第2笔数据, ..., 字段1第p1笔数据],
               [字段2第1笔数据, 字段2第2笔数据, ..., 字段2第p1笔数据],
               ...
              ],
     客户号2: [[字段1第1笔数据, 字段1第2笔数据, ..., 字段1第p2笔数据],
               [字段2第1笔数据, 字段2第2笔数据, ..., 字段2第p2笔数据],
               ...
              ],
     ...,
    }

    产品签约表数据保存格式为(假定用户i在n ~ n+m-1月内共签约qi款产品)：
    {客户号1: [[字段1第1笔数据, 字段1第2笔数据, ..., 字段1第q1笔数据],
               [字段2第1笔数据, 字段2第2笔数据, ..., 字段2第q1笔数据],
               ...
              ],
     客户号2: [[字段1第1笔数据, 字段1第2笔数据, ..., 字段1第q2笔数据],
               [字段2第1笔数据, 字段2第2笔数据, ..., 字段2第q2笔数据],
               ...
              ],
     ...,
    }
    '''
    def __init__(self, fieldName2fieldType):
        self.fieldProcessor = CMSBFieldProcessor(fieldName2fieldType)
        self.protolNumName = '协议号'
        self.custNumName = '我行客户号'

    def readLoans(self, filenames):
        '''
        读取贷款协议表数据

        Args:
            filenames (list): 文件名列表

        Returns:
            dict: 字段索引
            dict: 表数据
        '''
        fieldName2Index = {}
        loans = {}

        for i, filename in enumerate(filenames):
            with open(filename) as inFile:
                # 读取第一行
                firstLine = inFile.readline()
                if i == 0:  # 第一次读取文件
                    fieldNames = firstLine.strip().split('\t')  # 利用第一行获取所有字段
                    fieldName2Index = self.fieldProcessor.buildLoanFieldNameIndex(fieldNames)  # 构建字段索引
                # 读取剩余行，获取各字段对应数据
                for line in inFile:
                    fields = line.strip().split('\t')
                    fields = self.fieldProcessor.convertLoanFields(fields)
                    self.fieldProcessor.addLoanFields(fields, loans, self.protolNumName)
                inFile.close()
        loans = self.fieldProcessor.expandSamples(loans, self.protolNumName, fieldName2Index)  # 扩展字段维数

        return fieldName2Index, loans

    def readTranss(self, filenames):
        '''
        读取交易流水表数据

        Args:
            filenames (list): 文件名列表

        Returns:
            dict: 字段索引
            dict: 表数据
        '''
        fieldName2Index = {}
        transs = {}

        for i, filename in enumerate(filenames):
            with open(filename) as inFile:
                # 读取第一行
                firstLine = inFile.readline()
                if i == 0:  # 第一次读取文件
                    fieldNames = firstLine.strip().split('\t')  # 第一次读取，利用第一行获取所有字段
                    fieldName2Index = self.fieldProcessor.buildTransFieldNameIndex(fieldNames)  # 构建字段索引
                # 读取剩余行，获取各字段对应数据
                for line in inFile:
                    fields = line.strip().split('\t')
                    fields = self.fieldProcessor.convertTransFields(fields)
                    self.fieldProcessor.addTransFields(fields, transs, self.custNumName)
                inFile.close()

        return fieldName2Index, transs

    def readProds(self, filenames):
        '''
        读取产品签约表数据

        Args:
            filenames (list): 文件名列表

        Returns:
            dict: 字段索引
            dict: 表数据
        '''
        fieldName2Index = {}
        prods = {}

        for i, filename in enumerate(filenames):
            with open(filename) as inFile:
                # 读取第一行
                firstLine = inFile.readline()
                if i == 0:  # 第一次读取文件
                    fieldNames = firstLine.strip().split('\t')  # 第一次读取，利用第一行获取所有字段
                    fieldName2Index = self.fieldProcessor.buildProdFieldNameIndex(fieldNames)  # 构建字段索引
                # 读取剩余行，获取各字段对应数据
                for line in inFile:
                    fields = line.strip().split('\t')
                    fields = self.fieldProcessor.convertProdFields(fields)
                    self.fieldProcessor.addProdFields(fields, prods, self.custNumName)
                inFile.close()

        return fieldName2Index, prods
