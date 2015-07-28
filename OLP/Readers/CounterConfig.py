# -*- coding: utf-8 -*-
prodContactDateTitle = '签约时间'
prodContactCodeTitle = '零售签约产品代码'
loanNoTitle = '协议号'
custNoTitle = '我行客户号'
loanCustNoTitle = '核心客户号'
contactAmountTitle = '签约数量'

defaultDate = '0001/1/1'

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

