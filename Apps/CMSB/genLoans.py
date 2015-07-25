import random


chars = ['a', 'b', 'c', 'd', 'e', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         '0', '1', '2', '3', '4' ,'5', '6', '7', '8', '9']


def getRandIntGenerator(a, b):
    def genRandInt():
        return random.randint(a, b)
    return genRandInt


def getRandFltGenerator(a, b):
    def genRandFlt():
        return random.uniform(a, b)
    return genRandFlt


def getRandEltGenerator(elements):
    def genRandElt():
        return random.choice(elements)
    return genRandElt()


def getRandStrGenerator(len_):
    def genRandStr():
        str_ = ''
        for i in range(len_):
            str_ += random.choice(chars)
        return str_
    return genRandStr()


def getRandDateGenerator():
    def genRandDate():
        return '2014/02/10'


def getRandBoolGenerator():
    def genRandBool():
        return random.choice(['', '1'])


def genRandList(n):
    elts = set()
    for i in range(n):
        while True:
            eltLen = random.randint(1, 10)
            elt = ''
            for j in range(eltLen):
                elt += random.choice(chars)
            if ele not in elts:
                elts.add(elt)
                break
    return list(elts)


fieldNames2Generator = {
    # '协议号': getRandIntGenerator(100000000, 800000000),
    '协议修饰符': getRandEltGenerator(genRandList(2)),
    '币种': getRandEltGenerator(genRandList(2)),
    '值类型代码': getRandEltGenerator(genRandList(2)) ,
    '账务机构号': getRandEltGenerator(genRandList(2)),
    '一级分行机构号':  getRandEltGenerator(genRandList(2)),
    '零售贷款品种代码': getRandEltGenerator(genRandList(2)),
    # '核心客户号': getRandStrGenerator(15),
    'CUST_NAME': getRandStrGenerator(15),
    '项目编号': getRandStrGenerator(15),
    '项目类别代码': getRandEltGenerator(genRandList(2)),
    '主机产品代码': getRandEltGenerator(genRandList(2)),
    '担保方式代码': getRandEltGenerator(genRandList(2)),
    '担保方式细分代码': getRandEltGenerator(genRandList(2)),
    '中长期贷款标志': getRandEltGenerator(genRandList(2)),
    '委托贷款类别代码': getRandEltGenerator(genRandList(2)),
    '委托贷款标志': getRandEltGenerator(genRandList(2)),
    '零售委托贷款情况代码': getRandEltGenerator(genRandList(2)),
    '受托支付标志': getRandBoolGenerator(),
    '合同编号': getRandStrGenerator(15),
    '申请编号': getRandStrGenerator(15),
    '授信申请编号': getRandStrGenerator(15),
    '额度编号': getRandStrGenerator(15),
    '零售贷款授信协议号': getRandStrGenerator(15),
    '零售贷款授信协议修饰符': getRandEltGenerator(genRandList(2)),
    '贷款处置方式代码': getRandEltGenerator(genRandList(2)),
    '小微贷款申请人分类代码': getRandEltGenerator(genRandList(2)),
    '小微采录行业种类代码': getRandEltGenerator(genRandList(2)),
    '投向行业种类代码': getRandEltGenerator(genRandList(2)),
    '外报行业种类代码': getRandEltGenerator(genRandList(2)),
    '终审信贷柜员号': getRandStrGenerator(15),
    '主客户经理员工号': getRandStrGenerator(15),
    '分成比例': getRandFltGenerator(1000, 1000000),
    '放款渠道代码': getRandEltGenerator(genRandList(2)),
    '数据来源系统编号': getRandEltGenerator(genRandList(2)),
    '放款金额': getRandFltGenerator(1000, 1000000),
    '放款日期': getRandDateGenerator(),
    '本月放款金额': getRandFltGenerator(1000, 1000000),
    '贷款期限': getRandIntGenerator(10, 20),
    '期限周期代码': getRandEltGenerator(genRandList(2)),
    '起息日期': getRandDateGenerator(),
    '到期日期': getRandDateGenerator(),
    '总期数': getRandIntGenerator(10, 20),
    '当前期数': getRandIntGenerator(10, 20),
    '已还期数': getRandIntGenerator(10, 20),
    '欠款期数': getRandIntGenerator(10, 20),
    '剩余期限': getRandIntGenerator(10, 20),
    '未还期限': getRandIntGenerator(10, 20),
    '零售贷款用途代码': getRandEltGenerator(genRandList(2)),
    '随央行利率变动标志': getRandBoolGenerator(),
    '调息时点模式代码': getRandEltGenerator(genRandList(2)),
    '最近利率调整日期': getRandDateGenerator(),
    '基准利率': getRandFltGenerator(1000, 1000000),
    '利率浮动值': getRandFltGenerator(1000, 1000000),
    '利率浮动比例': getRandFltGenerator(1000, 1000000),
    '执行利率': getRandFltGenerator(1000, 1000000),
    '放款利率': getRandFltGenerator(1000, 1000000),
    '罚息执行利率': getRandFltGenerator(1000, 1000000),
    '罚息利率浮动比例': getRandFltGenerator(1000, 1000000),
    '还款间隔': getRandIntGenerator(10, 20),
    '还款间隔周期代码': getRandEltGenerator(genRandList(2)),
    '还款卡号': getRandStrGenerator(15),
    '还款卡号余额': getRandFltGenerator(1000, 1000000),
    '还款方式代码': getRandEltGenerator(genRandList(2)),
    '约定还款日': getRandDateGenerator(),
    '本月应还款日期': getRandDateGenerator(),
    '本月应还款金额': getRandFltGenerator(1000, 1000000),
    '近期应还款日期': getRandDateGenerator(),
    '近期应还款金额': getRandFltGenerator(1000, 1000000),
    '本月正常还款金额': getRandFltGenerator(1000, 1000000),
    '本月提前还款金额': getRandFltGenerator(1000, 1000000),
    '上次付款日期': getRandDateGenerator(),
    '提前付款标志': getRandBoolGenerator(),
    '最早欠款日期':getRandDateGenerator(),
    '最长一期逾期天数': getRandIntGenerator(10, 20),
    '最近欠款日期': getRandDateGenerator(),
    '最近欠款天数': getRandIntGenerator(10, 20),
    '最近本金欠款日期': getRandDateGenerator(),
    '累计逾期次数': getRandIntGenerator(10, 20),
    '本年逾期次数': getRandIntGenerator(10, 20),
    '贷款评级优先标准代码': getRandEltGenerator(genRandList(2)),
    '手工设置十级分类代码': getRandEltGenerator(genRandList(2)),
    '初分十级分类代码': getRandEltGenerator(genRandList(2)),
    '调整后十级分类代码': getRandEltGenerator(genRandList(2)),
    '额度下最差十级分类代码': getRandEltGenerator(genRandList(2)),
    '贷款形态分类来源代码': getRandEltGenerator(genRandList(2)),
    '分类日期': getRandDateGenerator(),
    '十级分类代码': getRandEltGenerator(genRandList(2)),
    '五级分类代码': getRandEltGenerator(genRandList(2)),
    '展期标志': getRandBoolGenerator(),
    '结清标志': getRandBoolGenerator(),
    '结清日期': getRandDateGenerator(),
    '剩余本金': getRandFltGenerator(1000, 1000000),
    '正常本金': getRandFltGenerator(1000, 1000000),
    '正常本金科目号': getRandEltGenerator(genRandList(2)),
    '逾期本金': getRandFltGenerator(1000, 1000000),
    '逾期本金科目号': getRandEltGenerator(genRandList(2)),
    '呆滞本金': getRandFltGenerator(1000, 1000000),
    '呆滞本金科目号': getRandEltGenerator(genRandList(2)),
    '呆账本金': getRandFltGenerator(1000, 1000000),
    '呆账本金科目号': getRandEltGenerator(genRandList(2)),
    '拖欠本金': getRandFltGenerator(1000, 1000000),
    '表内欠息': getRandFltGenerator(1000, 1000000),
    '表外欠息': getRandFltGenerator(1000, 1000000),
    '拖欠利息': getRandFltGenerator(1000, 1000000),
    '表内罚息': getRandFltGenerator(1000, 1000000),
    '表外罚息': getRandFltGenerator(1000, 1000000),
    '拖欠罚息': getRandFltGenerator(1000, 1000000),
    '核销本金': getRandFltGenerator(1000, 1000000),
    '核销利息': getRandFltGenerator(1000, 1000000),
    '计提截止日期': getRandDateGenerator(),
    '计提利息': getRandFltGenerator(1000, 1000000),
    '应计利息科目号': getRandEltGenerator(genRandList(2)),
    '应收利息': getRandFltGenerator(1000, 1000000),
    '应收利息科目号': getRandEltGenerator(genRandList(2)),
    '当期应还利息': getRandFltGenerator(1000, 1000000),
    '已还正常本金': getRandFltGenerator(1000, 1000000),
    '已还利息总额': getRandFltGenerator(1000, 1000000),
    '已还罚息总额': getRandFltGenerator(1000, 1000000),
    '已还逾期本金总额': getRandFltGenerator(1000, 1000000),
    '贷款月日均': getRandFltGenerator(1000, 1000000),
    '贷款季日均': getRandFltGenerator(1000, 1000000),
    '贷款年日均': getRandFltGenerator(1000, 1000000),
    '贷款近一年日均': getRandFltGenerator(1000, 1000000),
    '贷款近三个月日均': getRandFltGenerator(1000, 1000000),
}


def genLoans(protolNums, custNums, months):
    loans = {}
    for protolNum, custNum in zip(protolNums, custNums):
        loan = {}
        loan['协议号'] = protolNum
        loan['核心客户号'] = custNum

