# -*- coding: utf-8 -*-

import os


baseDir = '/home/lk/Bank/Data'
loanDir = os.path.join(baseDir, 'Loans')
transDir = os.path.join(baseDir, 'Transactions')
prodDir = os.path.join(baseDir, 'Products')

trainMonths = ['2014-2', '2014-3']
testMonths = ['2014-4', '2014-5']


fieldName2fieldType = {
    '核心客户号': str,
    '协议号': str,
    '还款卡号': str,
    '放款金额': float,
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
}
