# -*- coding: utf-8 -*-

from OLP.core.samples import Sample, Samples
from OLP.Readers.TransCounter import TransCounter
from OLP.Readers.ProdContactCounter import ProdContactCounter
from OLP.Readers.FeatureBuilder import FeatureBuilder
from OLP.Readers.LabelReader import LabelReader


class SamplesBuilder:
    '''
    通过一个用户的三张表生成sample类型数据并返回，通过调用buildSample
    '''
    def __init__(self, loanFieldName2Index, featLoans, featCustNum2ProtolNums, labelLoans, transFieldName2Index, featTranss, prodFieldName2Index, featProds):
        self.loanFieldName2Index = loanFieldName2Index
        self.featLoans = featLoans
        self.featCustNum2ProtolNums = featCustNum2ProtolNums
        self.labelLoans = labelLoans
        self.transFieldName2Index = transFieldName2Index
        self.featTranss = featTranss
        self.prodFieldName2Index = prodFieldName2Index
        self.featProds = featProds

    def buildSample(self):
        # 生成用户特征
        fieldName2Index, feats = self.genFeats(self.loanFieldName2Index, self.featLoans, self.featCustNum2ProtolNums,
                                               self.transFieldName2Index, self.featTranss,
                                               self.prodFieldName2Index, self.featProds)
        # 生成用户标签
        labels = self.genLabels(self.loanFieldName2Index, self.featLoans, self.labelLoans, self.featCustNum2ProtolNums)
        # 生成样本
        samples = self.genSamples(fieldName2Index, self.featCustNum2ProtolNums, feats, labels)
        return samples

    def genFeats(self, loanFieldName2Index, loans, custNum2ProtolNums, transFieldName2Index, transs, prodFieldName2Index, prods):
        '''
        为每笔贷款生成特征

        Args:
            loanFieldName2Index (dict): 贷款协议表字段索引
            loans (dict): 贷款协议表数据
            transFieldName2Index (dict): 交易流水表字段索引
            transs (dict): 交易流水表数据
            prodFieldName2Index (dict): 产品签约表字段索引
            prods (dict): 产品签约表数据

        Returns:
            dict: 特征字段索引
            list: 客户号和特征值，格式为:
                [
                  [客户号1, [特征值11, 特征值12, ...]],
                  [客户号2, [特征值21, 特征值22, ...]],
                  ...
                ]
        '''
        transFieldName2Index, transs = TransCounter((transFieldName2Index, transs)).countProp()
        prods = ProdContactCounter((prodFieldName2Index, prods), '2014/3/31').countProdContact()  # TODO
        builder = FeatureBuilder((loanFieldName2Index, loans, custNum2ProtolNums),
                             (transFieldName2Index, transs),
                             prods)
        fieldName2Index, feats = builder.buildFeature()
        feats.sort(key=lambda item: item[0])
        return fieldName2Index, feats

    def genLabels(self, loanFieldName2Index, featLoans, labelLoans, custNum2ProtolNums):
        '''
        为每笔贷款生成类别标签

        Args:
            loanFieldName2Index (dict): 贷款协议表字段索引
            featLoans (dict): 用于生成特征的贷款协议表数据
            labelLoans (dict): 用于生成标签的贷款协议表数据

        Returns:
            list: 客户号和类别标签，格式为:
                [
                [客户号1, 类别标签1],
                [客户号2, 类别标签2],
                ...
                ]
        '''
        reader = LabelReader((loanFieldName2Index, labelLoans, custNum2ProtolNums), featLoans)
        labels = reader.readLabel()
        labels.sort(key=lambda item: item[0])
        return labels

    def genSamples(self, x_indexes, cust_num_protol_nums, feats, labels):
        '''
        将原有数据记录转为Samples格式
        '''
        samples = Samples(x_indexes)
        for feat, label in zip(feats, labels):
            cust_num = feat[0]
            protol_nums = cust_num_protol_nums[cust_num]
            X = feat[1]
            y = label[1]
            sample = Sample(cust_num, protol_nums, X, y)
            samples.append(sample)
        return samples
