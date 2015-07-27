# -*- coding: utf-8 -*-

import os
from OLP.Readers.CMSBReaders import CMSBReader
import config as cf

def readData(cf):
    reader = CMSBReader(cf.fieldName2fieldType)
    
    trnFeatLoanFilenames = [os.path.join(cf.loanDir, month) for month in cf.trnFeatMonths]
    trnFeatTransFilenames = [os.path.join(cf.transDir, month) for month in cf.trnFeatMonths]
    trnFeatProdFilenames = [os.path.join(cf.prodDir, month) for month in cf.trnFeatMonths]
    trnLabelLoanFilenames = [os.path.join(cf.loanDir, month) for month in cf.trnLabelMonths]
    tstFeatLoanFilenames = [os.path.join(cf.loanDir, month) for month in cf.tstFeatMonths]
    tstFeatTransFilenames = [os.path.join(cf.transDir, month) for month in cf.tstFeatMonths]
    tstFeatProdFilenames = [os.path.join(cf.prodDir, month) for month in cf.tstFeatMonths]
    tstLabelLoanFilenames = [os.path.join(cf.loanDir, month) for month in cf.tstLabelMonths]
    
    trnFeatLoans = reader.readLoans(trnFeatLoanFilenames)
    trnFeatTranss = reader.readTranss(trnFeatTransFilenames)
    trnFeatProds = reader.readProds(trnFeatProdFilenames)
    trnLabelLoans = reader.readLoans(trnLabelLoanFilenames)


#
#labelReader = LabelReader()
#targets = labelReader.readLabel(loans, '协议号')
#
#
#reader.setTargets(targets)
#loanFieldName2Index, loans, transFieldName2Index, transs, prodFieldName2Index, prods = reader.read()
#
#
#
#trans = CMSBTransReader(['2014-2.txt',],'业务标识').read()
#UniPrinter().pprint(trans)
#countTrans = CountTrans(trans)
#countProp = countTrans.countProp()
#UniPrinter().pprint(countProp)
#
#targets = [['1', '1', '1'],
#           ['2', '2', '0']]
#months = ['2014-2', '2014-3']
#
#
#reader.read()

reader = CMSBReader(cf.fieldName2fieldType)
loanFieldName2Index, loans = reader.readLoans(['/home/lk/Bank/Data/Loans/2014-2', '/home/lk/Bank/Data/Loans/2014-3'])
for loan in loans.values():
    for name, index in loanFieldName2Index.items():
        print '%s:%s' % (name, str(loan[index])),
    print '\n', '-' * 20
transFieldName2Index, transs = reader.readTranss(['/home/lk/Bank/Data/Transactions/2014-2', '/home/lk/Bank/Data/Transactions/2014-3'])
for trans in transs.values():
    for name, index in transFieldName2Index.items():
        print '%s:%s' % (name, str(trans[index])),
    print '\n', '-' * 20
prodFieldName2Index, prods = reader.readProds(['/home/lk/Bank/Data/Products/2014-2'])
for prod in prods.values():
    for name, index in prodFieldName2Index.items():
        print '%s:%s' % (name, str(prod[index])),
    print '\n', '-' * 20
