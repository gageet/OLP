# -*- coding: utf-8 -*-

countRules = {'notCorpTotalMoney':{'formula':'sum',
                                   'title':'折人民币',
                                   'rules':{'借贷标志':'notCorporation'}
                                   },
              'notCorpTotalCount':{'formula':'count',
                                   'title':'折人民币',
                                   'rules':{'借贷标志':'notCorporation'}
                                   }
              }