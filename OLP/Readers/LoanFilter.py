# -*- coding: utf-8 -*-


class Filter(object):

    def filter(self, title2index, loans):
        raise NotImplementedError


class CleanedLoanFilter(Filter):

    cleanedFlag = '结清标志'

    def __init__(self):
        pass

    def filter(self, title2index, loans):
        '''
        we delete some records which obey this rule.
        '''
        for key, loan in loans.items():
            index = title2index[self.cleanedFlag]
            for i in range(len(loan[index])):
                if loan[index][i] == True:
                    del loans[key]
                    break
        return title2index, loans


class CustCodeFilter(Filter):

    fiveClassificationCode = '五级分类代码'

    def __init__(self):
        pass

    def filter(self, title2index, loans):
        '''
        we delete some records which obey this rule.
        '''
        for key, loan in loans.items():
            index = title2index[self.fiveClassificationCode]
            for i in range(len(loan[index])):
                if loan[index][i] != '五级分类代码3':
                    del loans[key]
                    break
        return title2index, loans


class ThisMonthLoanFilter(Filter):

    statData = '统计日期'
    lendingData = '放款日期'

    def __init__(self):
        pass

    def filter(self, title2index, loans):
        '''
        we delete some records which obey this rule.
        '''
        for key, loan in loans.items():
            index1 = title2index[self.statData]
            index2 = title2index[self.lendingData]
            for i in range(len(loan[index1])):
                if loan[index1][i] == '' or loan[index2][i] == '':
                    continue
                statDataList = loan[index1][i].split('/')
                lendingDataList = loan[index2][i].split('/')
                if statDataList[0] == lendingDataList[0] and statDataList[1] == lendingDataList[1]:
                    del loans[key]
                    break
        return title2index, loans


def getFilter(name, param={}):
    modName, clsName = name.rsplit('.', 1)
    mod = __import__(modName, globals(), locals(), [clsName], -1)
    cls = getattr(mod, clsName)
    filter_ = cls(**param)
    return filter_


if __name__ == '__main__':
    from OLP.Readers import CMSBReaders
    filenames = ['2014-02-28LoanInformation.txt', '2014-03-31LoanInformation.txt', '2014-04-30LoanInformation.txt', '2014-05-31LoanInformation.txt']
    s = CMSBReaders.CMSBLoanReader(filenames, '协议号')
    title2index, loans = s.read()

    #print(len(loans))
    filter1 = CleanedLoanFilter()
    filter2 = CustCodeFilter()
    filter3 = ThisMonthLoanFilter()

    loans = filter1.filter(title2index, loans)
    loans = filter2.filter(title2index, loans)
    loans = filter3.filter(title2index, loans)

    #print loans
    #print(len(loans))
 
