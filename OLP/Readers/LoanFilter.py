# -*- coding: utf-8 -*-


class Filter(object):

    def filter(self, title2index, loans, custo2protol):
        raise NotImplementedError

class CleanedLoanFilter(Filter):
    '''
    每个Filter类执行一条过滤规则，删除n条协议
    读入值和返回值都是 (title2index,loans,custo2protol)
    '''
    cleanedFlag = '结清标志'
    customID = '核心客户号'

    def __init__(self):
        pass

    def filter(self, title2index, loans, custo2protol):
        '''
        we delete some records which obey the rule of cleanedFlag.
        '''
        # UniPrinter().pprint(title2index)
        for key, loan in loans.items():
            index = title2index[self.cleanedFlag]
            customIndex = title2index[self.customID]
            for i in range(len(loan[index])):
                if loan[index][i] == True:
                    del loans[key]
                    values = custo2protol.get(loan[customIndex][i])
                    values.remove(key)
                    custo2protol[loan[customIndex][i]] = values
                    break
        return title2index, loans, custo2protol


class CustCodeFilter(Filter):

    fiveClassificationCode = '五级分类代码'
    customID = '核心客户号'

    def __init__(self):
        pass

    def filter(self, title2index, loans, custo2protol):
        '''
        we delete some records which obey the rule of fiveClassificationCode.
        '''
        for key, loan in loans.items():
            index = title2index[self.fiveClassificationCode]
            customIndex = title2index[self.customID]
            for i in range(len(loan[index])):
                if loan[index][i] != '五级分类代码3':
                    del loans[key]
                    values = custo2protol.get(loan[customIndex][i])
                    values.remove(key)
                    custo2protol[loan[customIndex][i]] = values
                    break
        return title2index, loans, custo2protol


class ThisMonthLoanFilter(Filter):

    statData = '统计日期'
    lendingData = '放款日期'
    customID = '核心客户号'

    def __init__(self):
        pass

    def filter(self, title2index, loans, custo2protol):
        '''
        we delete some records which obey this rule.
        '''
        for key, loan in loans.items():
            index1 = title2index[self.statData]
            index2 = title2index[self.lendingData]
            customIndex = title2index[self.customID]

            for i in range(len(loan[index1])):
                if loan[index1][i] == '' or loan[index2][i] == '':
                    continue
                statDataList = loan[index1][i].split('/')
                lendingDataList = loan[index2][i].split('/')
                if statDataList[0] == lendingDataList[0] and statDataList[1] == lendingDataList[1]:
                    del loans[key]
                    values = custo2protol.get(loan[customIndex][i])
                    values.remove(key)
                    custo2protol[loan[customIndex][i]] = values
                    break
        return title2index, loans, custo2protol


def getFilter(name, param={}):
    modName, clsName = name.rsplit('.', 1)
    mod = __import__(modName, globals(), locals(), [clsName], -1)
    cls = getattr(mod, clsName)
    filter_ = cls(**param)
    return filter_


if __name__ == '__main__':
    '''
    main函数为测试代码，实际运行中不需要。
    '''

    from OLP.Readers.CMSBReaders import CMSBReader
    import config

    filenames = ['2014-02-28LoanInformation.txt', '2014-03-31LoanInformation.txt', '2014-04-30LoanInformation.txt', '2014-05-31LoanInformation.txt']
    s = CMSBReader(config.fieldName2fieldType)
    title2index, loans, custo2protol = s.readLoans(filenames)

    print(len(loans))
    print(custo2protol)
    filter1 = CleanedLoanFilter()
    filter2 = CustCodeFilter()
    filter3 = ThisMonthLoanFilter()

    title2index, loans, custo2protol = filter1.filter(title2index, loans, custo2protol)
    title2index, loans, custo2protol = filter2.filter(title2index, loans, custo2protol)
    title2index, loans, custo2protol = filter3.filter(title2index, loans, custo2protol)

    #print loans
    print(len(loans))
    print(custo2protol)
 
