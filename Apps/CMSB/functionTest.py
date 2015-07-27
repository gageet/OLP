from OLP.Readers.CMSBReaders import CMSBReader
import config
from OLP.Readers.ReaderTools import UniPrinter
from OLP.Readers.ProdContactCounter import ProdContactCounter

tableObject = CMSBReader(config.fieldName2fieldType)
table = tableObject.readProds(['prods.txt',])
UniPrinter().pprint(table)
tableFiltered = ProdContactCounter(table, config.trnFeatMonths[-1]+'/31').countProdContact()
UniPrinter().pprint(tableFiltered)