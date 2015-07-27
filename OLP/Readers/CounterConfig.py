# -*- coding: utf-8 -*-
prodContactDateTitle = '签约时间'
prodContactCodeTitle = '零售签约产品代码'
loanNoTitle = '协议号'
custNoTitle = '我行客户号'
loanCustNoTitle = '核心客户号'
contactAmountTitle = '签约数量'

defaultDate = '0001/1/1'

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

