# -*- coding: utf-8 -*-
import os

class LoanTableReader:
    '''
    the LoanTableReader
    '''

    def __init__(self, loanTablePathList):
        self.loanTablePathList = loanTablePathList
        pass

    def read(self):
        """
        Read the loanTable.
        :param loanTablePathList: a list[] that contains all loanTablePaths
        :return: a list[] that contains all the elements that contained in loanTable
        """
        wholeLoanTable = []
        for loanTablePath in self.loanTablePathList:
            loanTable = []
            loanTableObject = open(loanTablePath)
            tableKey = []
            lineNum = 0
            for line in loanTableObject:
                if lineNum == 0:
                    tableKey = [_.decode('utf-8') for _ in line.strip().split('\t')]
                    lineNum = 1
                else:
                    print tableKey[0]
                    tableValue = line.strip().split('\t')
                    tableDict = {}
                    for elementNum in range(len(tableKey)):
                        tableDict[tableKey[elementNum]] = tableValue[elementNum]
                    loanTable.append(tableDict)
            wholeLoanTable.extend(loanTable)
        return wholeLoanTable

if __name__ == '__main__':
    print os.path.dirname(os.path.realpath(__file__))
    loanTable = LoanTableReader([os.path.dirname(os.path.realpath(__file__))+'\\2014-02-28.txt',])
    print loanTable.read()