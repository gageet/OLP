from OLP.Readers.CMSBReaders import CMSBReader
from OLP.Readers.LabelReader import LabelReader
import config as cf


reader = CMSBReader(None, cf.months, cf.loanDir, cf.transDir, cf.prodDir, cf.fieldName2fieldType)
loans = reader.readLoans(None, cf.loanDir, cf.months)

labelReader = LabelReader()
targets = labelReader.readLabel(loans, '协议号')


reader.setTargets(targets)
loanFieldName2Index, loans, transFieldName2Index, transs, prodFieldName2Index, prods = reader.read()



trans = CMSBTransReader(['2014-2.txt',],'业务标识').read()
UniPrinter().pprint(trans)
countTrans = CountTrans(trans)
countProp = countTrans.countProp()
UniPrinter().pprint(countProp)

targets = [['1', '1', '1'],
           ['2', '2', '0']]
months = ['2014-2', '2014-3']


reader.read()
