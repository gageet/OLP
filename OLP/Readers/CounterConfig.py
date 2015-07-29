# -*- coding: utf-8 -*-

'''
配置文件
'''

# 用户产品签约表
# title
prodContactDateTitle = '签约时间'
prodContactCodeTitle = '零售签约产品代码'
# 签约表生成的feature（签约数量）的 title
contactAmountTitle = '签约数量'

# 用户产品签约表、用户交易流水表中的客户号title
custNoTitle = '我行客户号'

# 贷款表
# 客户号title
loanCustNoTitle = '核心客户号'
# 协议号title
loanNoTitle = '协议号'

debtDate = '最近欠款日期'
statDate = '统计日期'
lastRepayDate = '上次付款日期'
shouldRepayDate = '本月应还款日期'
# 默认时间，可能会在prodContactCounter统计时间用到
defaultDate = '0001/1/1'

# 提取feature时，提取贷款表中下列title的特征
loanfeatTitle = {
    '核心客户号': str,
    '协议号': str,
    '还款卡号': str,
    '放款金额': float,
    '统计日期': str,
    '放款日期': str,
    '已还期数': float,
    '欠款期数': float,
    '剩余期限': float,
    '还款卡号余额': float,
    '本月应还款金额': float,
    '最长一期逾期天数': float,
    '最近欠款天数': float,
    '累计逾期次数': float,
    '本年逾期次数': float,
    '剩余本金': float,
    '正常本金': float,
    '逾期本金': float,
    '当期应还利息': float,
    '已还正常本金': float,
    '已还利息总额': float,
    '已还罚息总额': float,
    '已还逾期本金总额': float,
    '贷款月日均': float,
    '贷款季日均': float,
    '贷款年日均': float,
    '结清标志': bool,
    '五级分类代码': str
}

# 统计交易流水表中的下列属性，作为该表特征
# 格式：{属性名：{
# 'formula':'sum/count/average', # 统计公式：求和/统计次数/平均值
# 'title':'折人民币',  # 统计哪一项
# 'rules':{title1: value1,title2: value2 # 统计的筛选条件
# }}
countRules = {'notCorpIncomeTotalMoney':{'formula':'sum',
                                   'title':'折人民币',
                                   'rules':{'借贷标志':True,'客户类型':'客户类型2'}
                                   },
              'notCorpIncomeTotalCount':{'formula':'count',
                                   'title':'折人民币',
                                   'rules':{'借贷标志':True,'客户类型':'客户类型2'}
                                   },
              'notCorpIncomeAvg':{'formula':'average',
                                   'title':'折人民币',
                                   'rules':{'借贷标志':True,'客户类型':'客户类型2'}
                                   },
              'notCorpOutcomeTotalMoney':{'formula':'sum',
                                   'title':'折人民币',
                                   'rules':{'借贷标志':True,'客户类型':'客户类型2'}
                                   },
              'notCorpOutcomeTotalCount':{'formula':'count',
                                   'title':'折人民币',
                                   'rules':{'借贷标志':True,'客户类型':'客户类型2'}
                                   },
              'notCorpOutcomeAvg':{'formula':'average',
                                   'title':'折人民币',
                                   'rules':{'借贷标志':True,'客户类型':'客户类型2'}
                                   },
              'notCorpOurBankRivalIncomeTotalMoney':{'formula':'sum',
                                                       'title':'折人民币',
                                                       'rules':{'借贷标志':False,'客户类型':'客户类型3','对方是否我行客户':True}
                                                       },
              'notCorpOurBankRivalIncomeTotalCount':{'formula':'count',
                                                       'title':'折人民币',
                                                       'rules':{'借贷标志':False,'客户类型':'客户类型3','对方是否我行客户':True}
                                                       },
              'notCorpOurBankRivalIncomeAvg':{'formula':'average',
                                                 'title':'折人民币',
                                                 'rules':{'借贷标志':False,'客户类型':'客户类型3','对方是否我行客户':True}
                                                 },
              'CorpIncomeTotalMoney':{'formula':'sum',
                                   'title':'折人民币',
                                   'rules':{'借贷标志':False,'客户类型':'客户类型3'}
                                   },
              'CorpIncomeTotalCount':{'formula':'count',
                                   'title':'折人民币',
                                   'rules':{'借贷标志':False,'客户类型':'客户类型3'}
                                   },
              'CorpIncomeAvg':{'formula':'average',
                               'title':'折人民币',
                               'rules':{'借贷标志':False,'客户类型':'客户类型3'}
                              },
               'CorpOurBankRivalIncomeTotalMoney':{'formula':'sum',
                                                       'title':'折人民币',
                                                       'rules':{'借贷标志':False,'客户类型':'客户类型1','对方是否我行客户':True}
                                                       },
              'CorpOurBankRivalIncomeTotalCount':{'formula':'count',
                                                       'title':'折人民币',
                                                       'rules':{'借贷标志':False,'客户类型':'客户类型1','对方是否我行客户':True}
                                                       },
              'CorpOurBankRivalIncomeAvg':{'formula':'average',
                                                 'title':'折人民币',
                                                 'rules':{'借贷标志':False,'客户类型':'客户类型1','对方是否我行客户':False}
                                                 },
              }

