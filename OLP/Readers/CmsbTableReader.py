# -*- coding: utf-8 -*-
class TableReader:

	def __init__(self):
		pass
	def readTransSingleFile(self,filename):
		print(filename)
		dataMat = []
		featureName = []
		dictArr = dict()
		fr = open(filename)
		flag = 1
		for line in fr.readlines():
			if flag:
				sv = line.strip('\n').split('\t')
				featureName = sv
				flag = 0
				continue
			else:
				sv = line.strip('\n').split('\t')
				for i in range(len(featureName)):
					dictArr[featureName[i]] = sv[i]
				dataMat.append(dictArr)
		return dataMat
	def transTableReader(self,fileList):
		m = len(fileList)
		transactionsMat = []
		for i in range(m):
			fileNameStr = fileList[i]
			transactionsMat.extend(self.readTransSingleFile(fileNameStr))
		return transactionsMat


# if __name__ == '__main__':
# 	s = TableReader()
# 	dataMat = s.transTableReader(['microloanCustTrans2014-02-28.txt','microloanCustTrans2014-03-31.txt'])
# 	print(dataMat)