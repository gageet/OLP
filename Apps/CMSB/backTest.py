# -*- coding: utf-8 -*-

import os
import numpy as np
from OLP.Readers.ReaderTools import UniPrinter
from OLP.Readers.CMSBReaders import CMSBReader
from OLP.Readers.LoanFilter import getFilter
from OLP.Readers.FeatureBuilder import FeatureBuilder
from OLP.Readers.ProdContactCounter import ProdContactCounter
from OLP.Readers.TransCounter import TransCounter
from OLP.Readers.LabelReader import LabelReader
from OLP.core.sample import Sample, Samples
from OLP.Models.Classifier import getClassifier
from OLP.Metrics.Metric import getMetric
import config as cf


def filterLoans(filterNames, fieldName2Index, loans):
    '''
    根据指定规则过滤贷款协议数据

    Args:
        filterNames (list): 过滤器名称列表
        fieldName2Index (dict): 贷款协议表字段索引
        loans (dict): 贷款协议表数据

    Returns:
        dict: 过滤后的贷款协议表数据
    '''
    filters = [getFilter(filterName) for filterName in filterNames]
    for filter_ in filters:
        fieldName2Index, loans = filter_.filter(fieldName2Index, loans)
    return loans


def genFeats(loanFieldName2Index, loans,
             transFieldName2Index, transs,
             prodFieldName2Index, prods):
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
    prods = ProdContactCounter((prodFieldName2Index, prods), '2014/3/31').countProdContact()
    builder = FeatureBuilder((loanFieldName2Index, loans),
                             (transFieldName2Index, transs),
                             prods)
    fieldName2Index, feats = builder.buildFeature()
    feats.sort(key=lambda item: item[0])
    return fieldName2Index, feats


def genLabels(loanFieldName2Index, featLoans, labelLoans):
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
    reader = LabelReader((loanFieldName2Index, labelLoans), featLoans)
    labels = reader.readLabel()
    labels.sort(key=lambda item: item[0])
    return labels


def gen_samples(field_indexes, custNum2ProtolNums, feats, labels):
    samples = Samples(field_indexes)
    for feat, label in zip(feats, labels):
        cust_num = feat[0]
        protol_nums = custNum2ProtolNums[cust_num]
        X = feat[1]
        y = label[1]
        sample = Sample(field_indexes, cust_num, protol_nums, X, y)
        samples.add(sample)
    return samples


def analyze_samples(samples):
    pass


def genFeatImportances(fieldName2Index, feats, labels):
    '''
    计算特征重要性

    Args:
        fieldName2Index (dict): 字段索引
        feats (list): 客户号和特征值，格式为:
                      [
                          [客户号1, [特征值11, 特征值12, ...]],
                          [客户号2, [特征值21, 特征值22, ...]],
                          ...
                      ]
        labels (list): 客户号和类别标签，格式为:
                       [
                           [客户号1, 类别标签1],
                           [客户号2, 类别标签2],
                           ...
                       ]

    Returns:
        dict: 特征重要性，格式为{特征1: 重要性1, 特征2: 重要性2, ...}
    '''
    modelName = 'OLP.Models.Ensemble.RandomForestClassifier'
    modelParam = {'nEstimators': 100}
    clf = getClassifier(modelName, modelParam)
    Xs = [_[1] for _ in feats]
    ys = [_[1] for _ in labels]
    clf.fit(Xs, ys)

    importrances = clf.getFeatImportances()
    fieldName2Importance = {}
    for fieldName, index in fieldName2Index.iteritems():
        fieldName2Importance[fieldName] = importrances[index]

    return fieldName2Importance


def statFeats(feats, labels):
    '''
    计算正常客户的特征均值与标准差
    '''
    avgFeats = []
    stdFeats = []
    for i in range(len(feats[0][1])):  # 遍历所有特征
        xs = [feats[j][1][i] for j in range(len(feats)) if labels[j][1] == 0]  # 所有正常用户的第i个特征
        mean = np.mean(xs)
        std = np.std(xs)
        avgFeats.append(mean)
        stdFeats.append(std)

    return avgFeats, stdFeats


def fit_model(clf, samples):
    '''
    训练模型

    Args:
        clf (Classifier): 待训练的分类器
        samples (Samples): 训练样本

    Returns:
        Classifier: 训练后的分类器
    '''
    Xs = samples.get_Xs()
    ys = samples.get_ys()
    clf.fit(Xs, ys)
    return clf


def predict_labels(clf, samples):
    '''
    预测分类标签

    Args:
        clf (Classifier): 训练后的分类器
        samples (Samples): 待预测样本

    Returns:
        samples (Samples): 预测后的样本
    '''
    Xs = samples.get_Xs()
    ys = clf.predict(Xs)
    for i, sample in enumerate(samples):
        sample.set_y_pred(ys[i])
    return samples


def genReport(metricNames, labels, labelsPred):
    '''
    生成模型评估报告

    Args:
        metricNames (list): 指标名称列表
        labels (list): 客户号和类别标签，格式为:
                       [
                           [客户号1, 类别标签1],
                           [客户号2, 类别标签2],
                           ...
                       ]
        labelsPred (list): 客户号和类别标签，格式为:
                           [
                               [客户号1, 类别标签1],
                               [客户号2, 类别标签2],
                               ...
                           ]

    Returns:
        str: 模型评估报告
    '''
    reports = ''
    ys = [_[1] for _ in labels]
    ysPred = [_[1] for _ in labelsPred]
    metrics = [getMetric(metricName) for metricName in metricNames]
    for metric in metrics:
        ret = metric.get(ys, ysPred)
        reports += metric.format(ret) + '\n'
    return reports


def saveSamples(fieldName2Index, custNum2ProtolNums, feats, labels, filename):
    '''
    保存样本

    Args:
        fieldName2Index (dict): 字段索引
        feats (list): 客户号和特征值，格式为:
                      [
                          [客户号1, [特征值11, 特征值12, ...]],
                          [客户号2, [特征值21, 特征值22, ...]],
                          ...
                      ]
        labels (list): 客户号和类别标签，格式为:
                       [
                           [客户号1, 类别标签1],
                           [客户号2, 类别标签2],
                           ...
                       ]
        filename (str): 文件名
    '''

    items = fieldName2Index.items()
    items.sort(key=lambda item: item[1])

    with open(filename, 'w') as outFile:
        outFile.write('\t'.join(['是否逾期', '客户号', '协议号'] + [item[0] for item in items]))
        outFile.write('\n')
        for feat, label in zip(feats, labels):
            custNum = label[0]
            protolNums = custNum2ProtolNums[custNum]
            X = feat[1]
            y = label[1]
            outFile.write('%d' % y)
            outFile.write('\t%s' % custNum)
            outFile.write('\t%s' % ','.join(protolNums))
            for fieldName, index in items:
                outFile.write('\t%.4f' % X[index])
            outFile.write('\n')


def backTest():
    '''
    回测
    '''
    # 读入贷款协议数据，交易流水数据和签约产品数据
    reader = CMSBReader(cf.fieldName2fieldType)

    trnFeatLoanFilenames = [os.path.join(cf.loanDir, month) for month in cf.trnFeatMonths]
    trnFeatTransFilenames = [os.path.join(cf.transDir, month) for month in cf.trnFeatMonths]
    trnFeatProdFilenames = [os.path.join(cf.prodDir, month) for month in cf.trnFeatMonths]
    trnLabelLoanFilenames = [os.path.join(cf.loanDir, month) for month in cf.trnLabelMonths]
    tstFeatLoanFilenames = [os.path.join(cf.loanDir, month) for month in cf.tstFeatMonths]
    tstFeatTransFilenames = [os.path.join(cf.transDir, month) for month in cf.tstFeatMonths]
    tstFeatProdFilenames = [os.path.join(cf.prodDir, month) for month in cf.tstFeatMonths]
    tstLabelLoanFilenames = [os.path.join(cf.loanDir, month) for month in cf.tstLabelMonths]

    loanFieldName2Index, trnFeatLoans, trnFeatCustNum2ProtolNums = reader.readLoans(trnFeatLoanFilenames)
    transFieldName2Index, trnFeatTranss = reader.readTranss(trnFeatTransFilenames)
    prodFieldName2Index, trnFeatProds = reader.readProds(trnFeatProdFilenames)
    loanFieldName2Index, trnLabelLoans, trnLabelCustNum2ProtolNums = reader.readLoans(trnLabelLoanFilenames)
    loanFieldName2Index, tstFeatLoans, tstFeatCustNum2ProtolNums = reader.readLoans(tstFeatLoanFilenames)
    transFieldName2Index, tstFeatTranss = reader.readTranss(tstFeatTransFilenames)
    prodFieldName2Index, tstFeatProds = reader.readProds(tstFeatProdFilenames)
    loanFieldName2Index, tstLabelLoans, tstLabelCustNum2ProtolNums = reader.readLoans(tstLabelLoanFilenames)

    # 过滤贷款协议数据
    trnFeatLoans = filterLoans(cf.filterNames, loanFieldName2Index, trnFeatLoans)
    tstFeatLoans = filterLoans(cf.filterNames, loanFieldName2Index, tstFeatLoans)

    # ----------------------------------------------------------------------
    # 生成用户特征
    fieldName2Index, trnFeats = genFeats(loanFieldName2Index, trnFeatLoans,
                                         transFieldName2Index, trnFeatTranss,
                                         prodFieldName2Index, trnFeatProds)
    fieldName2Index, tstFeats = genFeats(loanFieldName2Index, tstFeatLoans,
                                         transFieldName2Index, tstFeatTranss,
                                         prodFieldName2Index, tstFeatProds)

    # 生成用户标签
    trnLabels = genLabels(loanFieldName2Index, trnFeatLoans, trnLabelLoans)
    tstLabels = genLabels(loanFieldName2Index, tstFeatLoans, tstLabelLoans)

    # 生成样本
    trn_samples = gen_samples(fieldName2Index, trnFeatCustNum2ProtolNums, trnFeats. trnLabels)
    tst_samples = gen_samples(fieldName2Index, tstFeatCustNum2ProtolNums, tstFeats, tstLabels)

    # ----------------------------------------------------------------------
    # 计算特征重要性
    # fieldName2Importance = genFeatImportances(fieldName2Index, trnFeats, trnLabels)
    # UniPrinter().pprint(fieldName2Importance)

    # 训练模型并预测
    clf = getClassifier(cf.modelName, cf.modelParam)
    fit_model(clf, trn_samples)
    predict_labels(clf, tst_samples)

    # 保存样本
    trn_samples.save(cf.trnSampFilename)
    tst_samples.save(cf.tstSampFilename)

    # 计算评价指标
    # reports = genReport(cf.metricNames, tstLabels, tstLabelsPred)
    # print reports


def predict():
    '''
    预测
    '''
    # 读入贷款协议数据，交易流水数据和签约产品数据
    reader = CMSBReader(cf.fieldName2fieldType)

    trnFeatLoanFilenames = [os.path.join(cf.loanDir, month) for month in cf.trnFeatMonths]
    trnFeatTransFilenames = [os.path.join(cf.transDir, month) for month in cf.trnFeatMonths]
    trnFeatProdFilenames = [os.path.join(cf.prodDir, month) for month in cf.trnFeatMonths]
    trnLabelLoanFilenames = [os.path.join(cf.loanDir, month) for month in cf.trnLabelMonths]
    tstFeatLoanFilenames = [os.path.join(cf.loanDir, month) for month in cf.tstFeatMonths]
    tstFeatTransFilenames = [os.path.join(cf.transDir, month) for month in cf.tstFeatMonths]
    tstFeatProdFilenames = [os.path.join(cf.prodDir, month) for month in cf.tstFeatMonths]

    loanFieldName2Index, trnFeatLoans = reader.readLoans(trnFeatLoanFilenames)
    transFieldName2Index, trnFeatTranss = reader.readTranss(trnFeatTransFilenames)
    prodFieldName2Index, trnFeatProds = reader.readProds(trnFeatProdFilenames)
    loanFieldName2Index, trnLabelLoans = reader.readLoans(trnLabelLoanFilenames)
    loanFieldName2Index, tstFeatLoans = reader.readLoans(tstFeatLoanFilenames)
    transFieldName2Index, tstFeatTranss = reader.readTranss(tstFeatTransFilenames)
    prodFieldName2Index, tstFeatProds = reader.readProds(tstFeatProdFilenames)

    # 过滤贷款协议数据
    trnFeatLoans = filterLoans(loanFieldName2Index, trnFeatLoans)
    tstFeatLoans = filterLoans(loanFieldName2Index, tstFeatLoans)

    # 生成用户特征
    trnFeats = genFeats(loanFieldName2Index, trnFeatLoans,
                        transFieldName2Index, trnFeatTranss,
                        prodFieldName2Index, trnFeatProds)
    tstFeats = genFeats(loanFieldName2Index, tstFeatLoans,
                        transFieldName2Index, tstFeatTranss,
                        prodFieldName2Index, tstFeatProds)

    # 生成用户标签
    trnLabels = genLabels(loanFieldName2Index, trnFeatLoans, trnLabelLoans)

    # 训练模型并预测
    clf = getClassifier(cf.modelName, cf.modelParam)
    fit_model(clf, trnFeats, trnLabels)
    tstLabelsPred = predictLabels(clf, tstFeats)

    # 保存样本
    saveSamples(trnFeats, trnLabels, cf.trnSampFilename)
    saveSamples(tstFeats, tstLabelsPred, cf.tstSampFilename)


if __name__ == '__main__':

    backTest()
