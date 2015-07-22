# -*- coding: utf-8 -*-
import os
from OLP.Readers.Reader import Reader

class ContactReader(Reader):
    '''
    the Reader can read product contact table
    '''

    # Notice!!!
    # the class variable will be defined by the imported config file
    signedProdCode = 'signedProdCode'

    def __init__(self, filenames, primKey):
        self.filenames = filenames
        self.primKey = primKey

    def read(self):
        wholeTable = {}
        for tablePath in self.filenames:
            tableObject = open(tablePath)
            title2index = {}
            titleList = tableObject.readline().strip().split('\t')
            for index, title in enumerate(titleList):
                title2index[title] = index
            for index,value in enumerate(title2index):
                print index,value

            for tableRecord in tableObject:
                tableList = tableRecord.strip().split('\t')
                tableRecordKey = tableList[title2index[self.primKey]]
                tableRecordValue = tableList[title2index[self.signedProdCode]]

                if tableRecordKey in wholeTable:
                    wholeTable[tableRecordKey].append(tableRecordValue)
                else:
                    wholeTable[tableRecordKey] = [tableRecordValue,]
        return wholeTable


if __name__ == '__main__':
    print os.path.dirname(os.path.realpath(__file__))
    table = ContactReader([os.path.join(os.path.dirname(os.path.realpath(__file__)),'sighedTable.txt',)], 'custCode')
    loanTableList = table.read()
    print loanTableList