from OLP.Readers.CMSBReaders import CMSBReader
import config
from OLP.Readers.ReaderTools import UniPrinter
from OLP.Readers.FeatureBuilder import FeatureBuilder
from OLP.Readers.TransCounter import TransCounter
from OLP.Readers.ProdContactCounter import ProdContactCounter

#tableObject = CMSBReader(config.fieldName2fieldType)
#table = tableObject.readProds(['prods.txt',])
#UniPrinter().pprint(table)
#tableFiltered = ProdContactCounter(table, config.trnFeatMonths[-1]+'/31').countProdContact()
#UniPrinter().pprint(tableFiltered)

tableObject = CMSBReader(config.fieldName2fieldType)
loanTable = tableObject.readLoans(['loan.txt',])

transTable = tableObject.readTranss(['trans.txt',])
transCounter = TransCounter(transTable).countProp()

prodTable = tableObject.readProds(['prods.txt',])
prodCounter = ProdContactCounter(prodTable, config.trnFeatMonths[-1]+'/31').countProdContact()

UniPrinter().pprint(loanTable)
UniPrinter().pprint(transTable)
UniPrinter().pprint(prodTable)


fb = FeatureBuilder(loanTable, transCounter, prodCounter)
fbResult = fb.buildFeature()

UniPrinter().pprint(fbResult)


