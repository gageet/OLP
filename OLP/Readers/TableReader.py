# -*- coding: utf-8 -*-
import os

class TableReader:
    '''
    the Reader can read table
    '''

    def __init__(self):
        pass

    def readTable(self, tablePathList):
        """
        Read the table.
        :param tablePathList: a list[] that contains all TablePaths
        :return: a list[] that contains all the elements that contained in table
        """
        wholeTable = []
        for tablePath in tablePathList:

            if not os.path.exists(tablePath):
                raise IOError(tablePath)

            table = []
            tableObject = open(tablePath)
            tableKey = []
            lineNum = 0
            for line in tableObject:
                if lineNum == 0:
                    tableKey = line.strip().split('\t')
                    lineNum = 1
                else:
                    print tableKey[0]
                    tableValue = line.strip().split('\t')
                    tableDict = {}
                    for elementNum in range(len(tableKey)):
                        tableDict[tableKey[elementNum]] = tableValue[elementNum]
                    table.append(tableDict)
            wholeTable.extend(table)
        return wholeTable


if __name__ == '__main__':
    print os.path.dirname(os.path.realpath(__file__))
    table = TableReader()
    loanTableList = table.readTable([os.path.join(os.path.dirname(os.path.realpath(__file__)),'2014-02-28.txt',)])
    for dict in loanTableList:
        for key in dict:
            print key,dict[key]