from OLP.Readers.CMSBReaders import CMSBReader
import config as cf


reader = CMSBReader(cf.fieldName2fieldType)
loanFieldName2Index, loans = reader.readLoans('/home/lk/Bank/Data/Loans/2014-2')
for loan in loans.values():
    for name, index in loanFieldName2Index.items():
        print '%s:%s' % (name, str(loan[index])),
    print '\n', '-' * 20
transFieldName2Index, transs = reader.readTranss('/home/lk/Bank/Data/Transactions/2014-2')
for trans in transs.values():
    for name, index in transFieldName2Index.items():
        print '%s:%s' % (name, str(trans[index])),
    print '\n', '-' * 20
prodFieldName2Index, prods = reader.readProds('/home/lk/Bank/Data/Products/2014-2')
for prod in prods.values():
    for name, index in prodFieldName2Index.items():
        print '%s:%s' % (name, str(prod[index])),
    print '\n', '-' * 20
