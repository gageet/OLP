# -*- coding: utf-8 -*-
import random
import sys


chars = ['a', 'b', 'c', 'd', 'e', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


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
    return genRandElt


def getRandStrGenerator(len_):
    def genRandStr():
        str_ = ''
        for i in range(len_):
            str_ += random.choice(chars)
        return str_
    return genRandStr


def getRandDateGenerator():
    def genRandDate():
        return '2014/02/10'
    return genRandDate


def getRandBoolGenerator():
    def genRandBool():
        return random.choice(['', '1'])
    return genRandBool


def getRandEnumGenerator(fieldName):
    def genRandEnum():
        return fieldName + '%d' % random.choice([1, 2, 3])
    return genRandEnum


def genRandList(n):
    elts = set()
    for i in range(n):
        while True:
            eltLen = random.randint(1, 10)
            elt = ''
            for j in range(eltLen):
                elt += random.choice(chars)
            if elt not in elts:
                elts.add(elt)
                break
    return list(elts)


loanFieldNames2Generator = {
    # '协议号': getRandIntGenerator(100000000, 800000000),
    '协议修饰符': getRandEnumGenerator('协议修饰符'),
    '币种': getRandEnumGenerator('币种'),
    '值类型代码': getRandEnumGenerator('值类型代码'),
    '账务机构号': getRandEnumGenerator('服务机构号'),
    '一级分行机构号':  getRandEnumGenerator('一级分行机构号'),
    '零售贷款品种代码': getRandEnumGenerator('零售贷款品种代码'),
    # '核心客户号': getRandStrGenerator(15),
    'CUST_NAME': getRandStrGenerator(15),
    '项目编号': getRandStrGenerator(15),
    '项目类别代码': getRandEnumGenerator('项目类别代码'),
    '主机产品代码': getRandEnumGenerator('主机产品代码'),
    '担保方式代码': getRandEnumGenerator('担保方式代码'),
    '担保方式细分代码': getRandEnumGenerator('担保方式细分代码'),
    '中长期贷款标志': getRandEnumGenerator('中长期贷款标志'),
    '委托贷款类别代码': getRandEnumGenerator('委托贷款类别代码'),
    '委托贷款标志': getRandEnumGenerator('委托贷款标志'),
    '零售委托贷款情况代码': getRandEnumGenerator('零售委托贷款情况代码'),
    '受托支付标志': getRandBoolGenerator(),
    '合同编号': getRandStrGenerator(15),
    '申请编号': getRandStrGenerator(15),
    '授信申请编号': getRandStrGenerator(15),
    '额度编号': getRandStrGenerator(15),
    '零售贷款授信协议号': getRandStrGenerator(15),
    '零售贷款授信协议修饰符': getRandEnumGenerator('零售贷款授信协议修饰符'),
    '贷款处置方式代码': getRandEnumGenerator('贷款处置方式代码'),
    '小微贷款申请人分类代码': getRandEnumGenerator('小微贷款申请人分类代码'),
    '小微采录行业种类代码': getRandEnumGenerator('小微采录行业种类代码'),
    '投向行业种类代码': getRandEnumGenerator('投向行业种类代码'),
    '外报行业种类代码': getRandEnumGenerator('外报行业种类代码'),
    '终审信贷柜员号': getRandStrGenerator(15),
    '主客户经理员工号': getRandStrGenerator(15),
    '分成比例': getRandFltGenerator(1000, 1000000),
    '放款渠道代码': getRandEnumGenerator('放款渠道代码'),
    '数据来源系统编号': getRandEnumGenerator('数据来源系统编号'),
    '放款金额': getRandFltGenerator(1000, 1000000),
    '放款日期': getRandDateGenerator(),
    '本月放款金额': getRandFltGenerator(1000, 1000000),
    '贷款期限': getRandIntGenerator(10, 20),
    '期限周期代码': getRandEnumGenerator('期限周期代码'),
    '起息日期': getRandDateGenerator(),
    '到期日期': getRandDateGenerator(),
    '总期数': getRandIntGenerator(10, 20),
    '当前期数': getRandIntGenerator(10, 20),
    '已还期数': getRandIntGenerator(10, 20),
    '欠款期数': getRandIntGenerator(10, 20),
    '剩余期限': getRandIntGenerator(10, 20),
    '未还期限': getRandIntGenerator(10, 20),
    '零售贷款用途代码': getRandEnumGenerator('零售贷款用途代码'),
    '随央行利率变动标志': getRandBoolGenerator(),
    '调息时点模式代码': getRandEnumGenerator('调息时点模式代码'),
    '最近利率调整日期': getRandDateGenerator(),
    '基准利率': getRandFltGenerator(1000, 1000000),
    '利率浮动值': getRandFltGenerator(1000, 1000000),
    '利率浮动比例': getRandFltGenerator(1000, 1000000),
    '执行利率': getRandFltGenerator(1000, 1000000),
    '放款利率': getRandFltGenerator(1000, 1000000),
    '罚息执行利率': getRandFltGenerator(1000, 1000000),
    '罚息利率浮动比例': getRandFltGenerator(1000, 1000000),
    '还款间隔': getRandIntGenerator(10, 20),
    '还款间隔周期代码': getRandEnumGenerator('还款间隔周期代码'),
    '还款卡号': getRandStrGenerator(15),
    '还款卡号余额': getRandFltGenerator(1000, 1000000),
    '还款方式代码': getRandEnumGenerator('还款方式代码'),
    '约定还款日': getRandDateGenerator(),
    '本月应还款日期': getRandDateGenerator(),
    '本月应还款金额': getRandFltGenerator(1000, 1000000),
    '近期应还款日期': getRandDateGenerator(),
    '近期应还款金额': getRandFltGenerator(1000, 1000000),
    '本月正常还款金额': getRandFltGenerator(1000, 1000000),
    '本月提前还款金额': getRandFltGenerator(1000, 1000000),
    '上次付款日期': getRandDateGenerator(),
    '提前付款标志': getRandBoolGenerator(),
    '最早欠款日期': getRandDateGenerator(),
    '最长一期逾期天数': getRandIntGenerator(10, 20),
    '最近欠款日期': getRandDateGenerator(),
    '最近欠款天数': getRandIntGenerator(10, 20),
    '最近本金欠款日期': getRandDateGenerator(),
    '累计逾期次数': getRandIntGenerator(10, 20),
    '本年逾期次数': getRandIntGenerator(10, 20),
    '贷款评级优先标准代码': getRandEnumGenerator('贷款评级优先标准代码'),
    '手工设置十级分类代码': getRandEnumGenerator('手工设置十级分类代码'),
    '初分十级分类代码': getRandEnumGenerator('初分十级分类代码'),
    '调整后十级分类代码': getRandEnumGenerator('调整后十级分类代码'),
    '额度下最差十级分类代码': getRandEnumGenerator('额度下最差十级分类代码'),
    '贷款形态分类来源代码': getRandEnumGenerator('贷款形态分类来源代码'),
    '分类日期': getRandDateGenerator(),
    '十级分类代码': getRandEnumGenerator('十级分类代码'),
    '五级分类代码': getRandEnumGenerator('五级分类代码'),
    '展期标志': getRandBoolGenerator(),
    '结清标志': getRandBoolGenerator(),
    '结清日期': getRandDateGenerator(),
    '剩余本金': getRandFltGenerator(1000, 1000000),
    '正常本金': getRandFltGenerator(1000, 1000000),
    '正常本金科目号': getRandEnumGenerator('正常本金科目号'),
    '逾期本金': getRandFltGenerator(1000, 1000000),
    '逾期本金科目号': getRandEnumGenerator('逾期本金科目号'),
    '呆滞本金': getRandFltGenerator(1000, 1000000),
    '呆滞本金科目号': getRandEnumGenerator('呆滞本金科目号'),
    '呆账本金': getRandFltGenerator(1000, 1000000),
    '呆账本金科目号': getRandEnumGenerator('呆账本金科目号'),
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
    '应计利息科目号': getRandEnumGenerator('应计利息科目号'),
    '应收利息': getRandFltGenerator(1000, 1000000),
    '应收利息科目号': getRandEnumGenerator('应收利息科目号'),
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


transFieldNames2Generator = {
    '业务标识': getRandEnumGenerator('业务标识'),
    '核心主键': getRandStrGenerator(15),
    '流水号': getRandStrGenerator(15),
    '传票号': getRandStrGenerator(15),
    '交易机构': getRandEnumGenerator('交易机构'),
    '交易日期': getRandDateGenerator(),
    '交易时间': getRandDateGenerator(),
    '我行账户': getRandStrGenerator(15),
    # '我行客户号': getRandStrGenerator(15),
    '客户类型': getRandEnumGenerator('客户类型'),
    '交易代码': getRandEnumGenerator('交易代码'),
    '原交易代码': getRandEnumGenerator('原交易代码'),
    '业务类型': getRandEnumGenerator('业务类型'),
    '交易类型': getRandEnumGenerator('交易类型'),
    '借贷标志': getRandBoolGenerator(),
    '收付标志': getRandBoolGenerator(),
    '科目号': getRandEnumGenerator('科目号'),
    '币种': getRandEnumGenerator('币种'),
    '本外币标志': getRandBoolGenerator(),
    '原币交易金额': getRandFltGenerator(1000, 1000000),
    '折人民币': getRandFltGenerator(1000, 1000000),
    '折美元': getRandFltGenerator(1000, 1000000),
    '余额': getRandFltGenerator(1000, 1000000),
    '现/转标志': getRandBoolGenerator(),
    '汇款标志': getRandBoolGenerator(),
    '摘要': getRandStrGenerator(15),
    '是否跨境交易': getRandBoolGenerator(),
    '结算方式': getRandEnumGenerator('结算方式'),
    '用途': getRandStrGenerator(15),
    '对方系统': getRandEnumGenerator('对方系统'),
    '对方是否我行客户': getRandBoolGenerator(),
    '对方所在地区': getRandEnumGenerator('对方所在地区'),
    '对方行号类型': getRandEnumGenerator('对方行号类型'),
    '对方行号': getRandStrGenerator(15),
    '对方银行名称': getRandStrGenerator(15),
    '对方客户号': getRandStrGenerator(15),
    '对方名称': getRandStrGenerator(15),
    '对方账号': getRandStrGenerator(15),
    '对方交易日期': getRandDateGenerator(),
    '对方账户类型': getRandEnumGenerator('对方账户类型'),
    '对方证件类型': getRandEnumGenerator('对方证件类型'),
    '对方证件号码': getRandStrGenerator(15),
    '对方客户类型': getRandEnumGenerator('对方客户类型'),
    '抹账标志': getRandBoolGenerator(),
    '发生标志': getRandBoolGenerator(),
    '批量标志': getRandBoolGenerator(),
    '柜员': getRandStrGenerator(15),
    '是否需补录': getRandBoolGenerator(),
    '处理状态': getRandEnumGenerator('处理状态'),
    '当事人中文名称': getRandStrGenerator(15),
    '是否已补录': getRandBoolGenerator(),
    '补录时间': getRandDateGenerator(),
    '对方卡号': getRandStrGenerator(15),
    '凭证代码': getRandEnumGenerator('凭证代码'),
    '原客户号': getRandStrGenerator(15),
    '交易渠道': getRandEnumGenerator('交易渠道'),
    '是否计算': getRandBoolGenerator(),
    '是否规则': getRandBoolGenerator(),
    '事件类型': getRandEnumGenerator('事件类型'),
    '对方金融机构国家': getRandEnumGenerator('对方金融机构国家'),
    '网银IP地址': getRandStrGenerator(15),
    '交易去向国别': getRandEnumGenerator('交易去向国别'),
    '交易去向行政区': getRandEnumGenerator('交易去向行政区'),
    '交易发生地国别': getRandEnumGenerator('交易发生地国别'),
    '交易发生地行政区': getRandEnumGenerator('交易发生地行政区'),
    '代办人姓名': getRandStrGenerator(15),
    '代办人身份证件/证明文件类型': getRandEnumGenerator('代办人身份证件/证明文件类型'),
    '代办人身份证件/证明文件号码': getRandStrGenerator(15),
    '代办人国籍': getRandEnumGenerator('代办人国籍'),
    '金融机构和交易关系': getRandEnumGenerator('金融机构和交易关系'),
    '现钞标志': getRandBoolGenerator(),
    '对方人行客户类型': getRandEnumGenerator('对方人行客户类型'),
    '交易卡号': getRandStrGenerator(15),
    '上次更新柜员': getRandStrGenerator(15),
    '对方是否离岸账户': getRandBoolGenerator(),
    '业务代号': getRandStrGenerator(15),
    '大额验证状态': getRandEnumGenerator('大额验证状态'),
    '可疑验证状态': getRandEnumGenerator('可疑验证状态'),
    'ETL业务日期': getRandDateGenerator(),
}


def genData(nSamples, loanFilename, transFilename):
    protolNums = ['%d' % i for i in range(1, nSamples + 1)]
    custNums = ['%d' % i for i in range(1, nSamples + 1)]

    with open(loanFilename, 'w') as loanFile:
        fieldNames = loanFieldNames2Generator.keys()
        loanFile.write('\t'.join(['协议号', '核心客户号'] + fieldNames) + '\n')
        for protolNum, custNum in zip(protolNums, custNums):
            loanFile.write('%s\t%s' % (protolNum, custNum))
            for fieldName in fieldNames:
                field = loanFieldNames2Generator[fieldName]()
                loanFile.write('\t%s' % str(field))
            loanFile.write('\n')

    with open(transFilename, 'w') as transFile:
        fieldNames = transFieldNames2Generator.keys()
        transFile.write('\t'.join(['我行客户号'] + fieldNames) + '\n')
        for custNum in custNums:
            for transNum in range(random.randint(1, 10)):
                transFile.write('%s' % (custNum))
                for fieldName in fieldNames:
                    field = transFieldNames2Generator[fieldName]()
                    transFile.write('\t%s' % str(field))
                transFile.write('\n')

if __name__ == '__main__':
    nSamples = int(sys.argv[1])
    loanFilename = sys.argv[2]
    transFilename = sys.argv[3]
    genData(nSamples, loanFilename, transFilename)
