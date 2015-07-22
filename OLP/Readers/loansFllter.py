# -*- coding: utf-8 -*-

class Filter(object):

	def filter(self, title2index, loans):
		raise NotImplementedError


class cleanedLoansFilter(Filter):

	cleanedFlg = '结清标志'
	
	def __init__(self):
		pass

	def filter(self, title2index, loans):
		'''
		we delete some records which obey this rule.
		'''
		currLine = dict()
		loanList = loanTable
		for i in range(len(loanTable)):
			loan = loanTable[i]
			self.filtering(loan)

			statDataList = currLine[self.statData].split('/')
			lendingDataList = currLine[self.lendingData].split('/')
			if (currLine[self.cleanedFlg] == '0') or \
				(currLine[self.fiveClassificationCode] != '201') or \
				(statDataList[0] == lendingDataList[0] and statDataList[1] == lendingDataList[1]):
				del loanList[i]
		return	loanList


class CustCodeFilter(Filter):

	fiveClassificationCode = '五级分类代码'

	def __init__(self):
		pass

	def filter(self, title2index, loans):
		'''
		we delete some records which obey this rule.
		'''
		currLine = dict()
		loanList = loanTable
		for i in range(len(loanTable)):
			loan = loanTable[i]
			self.filtering(loan)

			statDataList = currLine[self.statData].split('/')
			lendingDataList = currLine[self.lendingData].split('/')
			if (currLine[self.cleanedFlg] == '0') or \
				(currLine[self.fiveClassificationCode] != '201') or \
				(statDataList[0] == lendingDataList[0] and statDataList[1] == lendingDataList[1]):
				del loanList[i]
		return	loanList

class thisMonthLoanFilter(Filter):

	statData = '统计日期'
	lendingData = '放款日期'

	def __init__(self):
		pass

	def filter(self, title2index, loans):
		'''
		we delete some records which obey this rule.
		'''
		currLine = dict()
		loanList = loanTable
		for i in range(len(loanTable)):
			loan = loanTable[i]
			self.filtering(loan)

			statDataList = currLine[self.statData].split('/')
			lendingDataList = currLine[self.lendingData].split('/')
			if (currLine[self.cleanedFlg] == '0') or \
				(currLine[self.fiveClassificationCode] != '201') or \
				(statDataList[0] == lendingDataList[0] and statDataList[1] == lendingDataList[1]):
				del loanList[i]
		return	loanList

if __name__ == '__main__':
	import CmsbTableReader
	s = CmsbTableReader.TableReader()
	dataMat = s.transTableReader(['2014-02-28LoanInformation.txt'])
	print(len(dataMat))
	print dataMat
	l = LoansFilter()
	loan = l.filter(dataMat)
	print(len(loan))
	print loan