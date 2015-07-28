# -*- coding: utf-8 -*-

import os
from OLP.Readers.ReaderTools import UniPrinter
from OLP.Readers.CMSBReaders import CMSBReader
from OLP.Readers.LoanFilter import getFilter
from OLP.Readers.FeatureBuilder import FeatureBuilder
from OLP.Readers.ProdContactCounter import ProdContactCounter
from OLP.Readers.TransCounter import TransCounter
from OLP.Readers.LabelReader import LabelReader
from OLP.Models.Classifier import getClassifier
from OLP.Metrics.Metric import getMetric
import config as cf


def filterLoans(filterNames, fieldName2Index, loans):
    filters = [getFilter(filterName) for filterName in filterNames]
    for filter_ in filters:
        fieldName2Index, loans = filter_.filter(fieldName2Index, loans)
    return loans


def genFeats(loanFieldName2Index, loans,
             transFieldName2Index, transs,
             prodFieldName2Index, prods):
    transFieldName2Index, transs = TransCounter((transFieldName2Index, transs)).countTrans()
    prodFieldName2Index, prods = ProdContactCounter((prodFieldName2Index, prods)).countProdContact()
    builder = FeatureBuilder((loanFieldName2Index, loans),
                             (transFieldName2Index, transs),
                             (prodFieldName2Index, prods))
    fieldName2Index, feats = builder.buildFeature()
    feats.sort(key=lambda item: item[0])
    return fieldName2Index, feats


def genLabels(loanFieldName2Index, featLoans, labelLoans):
    reader = LabelReader(labelLoans, featLoans)
    labels = reader.readLabel()
    labels.sort(key=lambda item: item[0])
    return labels


def fitModel(modelName, modelParam, feats, labels):
    Xs = [_[2] for _ in feats]
    ys = [_[2] for _ in labels]
    clf = getClassifier(modelName, modelParam)
    clf.fit(Xs, ys)
    return clf


def predictLabels(clf, feats):
    labels = []
    for protolNum, custNum, X in feats:
        y = clf.predict([X])[0]
        labels.append([protolNum, custNum, y])
    return labels


def genMetrics(metricNames, labels, labelsPred):
    reports = ''
    ys = [_[2] for _ in labels]
    ysPred = [_[2] for _ in labelsPred]
    metrics = [getMetric(metricName) for metricName in metricNames]
    for metric in metrics:
        ret = metric.get(ys, ysPred)
        reports += metric.format(ret) + '\n'
    return reports


def saveSamples(feats, labels, filename):
    with open(filename, 'w') as outFile:
        for feat, label in zip(feats, labels):
            outFile.write(feat[0])
            outFile.write('\t' + feat[1])
            for x in feat[2]:
                outFile.write('\t%.4f' % x)
            outFile.write('\t%.4f' % label[2])


def backTest():
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

    loanFieldName2Index, trnFeatLoans = reader.readLoans(trnFeatLoanFilenames)
    transFieldName2Index, trnFeatTranss = reader.readTranss(trnFeatTransFilenames)
    prodFieldName2Index, trnFeatProds = reader.readProds(trnFeatProdFilenames)
    loanFieldName2Index, trnLabelLoans = reader.readLoans(trnLabelLoanFilenames)
    loanFieldName2Index, tstFeatLoans = reader.readLoans(tstFeatLoanFilenames)
    transFieldName2Index, tstFeatTranss = reader.readTranss(tstFeatTransFilenames)
    prodFieldName2Index, tstFeatProds = reader.readProds(tstFeatProdFilenames)
    loanFieldName2Index, tstLabelLoans = reader.readLoans(tstLabelLoanFilenames)

    # 过滤贷款协议数据
    trnFeatLoans = filterLoans(loanFieldName2Index, trnFeatLoans)
    tstFeatLoans = filterLoans(loanFieldName2Index, tstFeatLoans)

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

    # 训练模型并预测
    clf = getClassifier(cf.modelName, cf.modelParam)
    fitModel(clf, trnFeats, trnLabels)
    tstLabelsPred = predictLabels(clf, tstFeats)

    # 保存样本
    saveSamples(fieldName2Index, trnFeats, trnLabels, cf.trnSampFilename)
    saveSamples(fieldName2Index, tstFeats, tstLabels, cf.tstSampFilename)
    saveSamples(fieldName2Index, tstFeats, tstLabelsPred, cf.predSampFilename)

    # 计算评价指标
    reports = genMetrics(cf.metricNames, tstLabels, tstLabelsPred)
    print reports


def predict():
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
    fitModel(clf, trnFeats, trnLabels)
    tstLabelsPred = predictLabels(clf, tstFeats)

    # 保存样本
    saveSamples(trnFeats, trnLabels, cf.trnSampFilename)
    saveSamples(tstFeats, tstLabelsPred, cf.tstSampFilename)


reader = CMSBReader(cf.fieldName2fieldType)

featLoanFilenames = [os.path.join(cf.loanDir, '2014-2'), os.path.join(cf.loanDir, '2014-3')]
fieldName2Index, loans = reader.readLoans(featLoanFilenames)
UniPrinter().pprint(loans)
