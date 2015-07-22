# -*- coding: utf-8 -*-
import os


baseDir = '/home/lk/Bank/SDK'

# 数据设置
dataDir = os.path.join(baseDir, 'Data')

loanDir = os.path.join(dataDir, 'Loans')

transDir = os.path.join(dataDir, 'Transactions')
microloanCustTransPath = os.path.join(transDir, 'microloanCustTrans')

prodDir = os.path.join(dataDir, 'Products')
microloanContractFormPath = os.path.join(prodDir, 'microloanContractForm.txt')

titleDir = os.path.join(dataDir, 'Titles')
loanTitleNecessityPath = os.path.join(titleDir, 'LoanTitleNecessity.txt')
loanTitlePresentPath = os.path.join(titleDir, 'LoanTitlePresent.txt')
transTitleNecessityPath = os.path.join(titleDir, 'TransactionTitleNecessity.txt')
transTitlePresentPath = os.path.join(titleDir, 'TransactionTitlePresent.txt')
prodTitleNecessityPath = os.path.join(titleDir, 'ProductTitleNecessity.txt')
prodTitlePresentPath = os.path.join(titleDir, 'ProductTitlePresent.txt')
dataCleanPath = os.path.join(titleDir, 'DataClean.txt')
dataLabelPath = os.path.join(titleDir, 'DataLabel.txt')

retDir = os.path.join(dataDir, 'Results')
featPath = os.path.join(retDir, 'Features.txt')
featImpPath = os.path.join(retDir, 'FeatureImportance.txt')
viewPath = os.path.join(retDir, 'ResultView.txt')

typeResultDir = os.path.join(dataDir, 'TypeResults')

typeCodeDir = os.path.join(dataDir, 'TypeResults')
featPosPath = os.path.join(typeCodeDir, 'FeaturePosition.txt')

finalInputDir = os.path.join(dataDir, 'FinalInput')

# 模型设置
modelDir = os.path.join(baseDir, 'Model')
modelType = 1
timeWindow = 3
trainWindow = 2
viewSize = 30
## 回测月份
months = ['2014-02-28', '2014-03-31', '2014-04-30', '2014-05-31']
##
feats = ['还款方式代码']
