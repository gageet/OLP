class Customer(object):

    def loa(self):
        raise NotImplementedError

    def build_sample(self):
        raise NotImplementedError


class CMSBCustomer(Customer):

fieldName2fieldType = {
    # 贷款表
    '核心客户号': str,
    '协议号': str,
    '还款卡号': str,
    '放款金额': float,
    '统计日期': str,
    '放款日期': str,
    '最近欠款日期': str,
    '上次付款日期': str,
    '本月应还款日期': str,
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
    '结清标志': _bool,
    '五级分类代码': str,
    # 流水表
    '我行客户号': str,
    '客户类型': str,  # enum
    '借贷标志': _bool,
    '折人民币': float,
    '汇款标志': _bool,
    '交易机构': str,  # enum
    '交易代码': str,  # enum
    '结算方式': str,  # enum
    '对方系统': str,  # enum
    '对方所在地区': str,  # enum
    '对方行号类型': str,  # enum
    '对方银行名称': str,
    '对方是否我行客户': _bool,
    '交易渠道': str,  # enum
    '交易发生地行政区': str,  # enum
    '交易去向行政区': str,  # enum
    # 产品表
    '我行客户号': str,
    '零售签约产品代码': str,
    '签约时间': str,
}


    def __init__(self):
        pass