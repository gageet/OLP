from OLP.Readers.CMSBReaders import CMSBReader
import config
from OLP.Readers.ReaderTools import UniPrinter
from OLP.Readers.FeatureBuilder import FeatureBuilder
from OLP.Readers.TransCounter import TransCounter
from OLP.Readers.ProdContactCounter import ProdContactCounter
from OLP.Readers.LoanCounter import LoanCounter

#tableObject = CMSBReader(config.fieldName2fieldType)
#table = tableObject.readProds(['prods.txt',])
#UniPrinter().pprint(table)
#tableFiltered = ProdContactCounter(table, config.trnFeatMonths[-1]+'/31').countProdContact()
#UniPrinter().pprint(tableFiltered)

tableObject = CMSBReader(config.fieldName2fieldType)
loanTable = tableObject.readLoans(['loan.txt','loan2.txt'])
loanCounter = LoanCounter(loanTable).countLoan()

transTable = tableObject.readTranss(['trans.txt',])
transCounter = TransCounter(transTable).countProp()

prodTable = tableObject.readProds(['prods.txt',])
prodCounter = ProdContactCounter(prodTable, config.trnFeatMonths[-1]+'/31').countProdContact()

UniPrinter().pprint(loanTable)
UniPrinter().pprint(transTable)
UniPrinter().pprint(prodTable)
print 'haha'
UniPrinter().pprint(loanCounter)
UniPrinter().pprint(transCounter)
UniPrinter().pprint(prodCounter)

fb = FeatureBuilder(loanCounter, transCounter, prodCounter)
fbResult = fb.buildFeature()
print 'hehe'
UniPrinter().pprint(fbResult)


