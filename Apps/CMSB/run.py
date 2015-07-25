from OLP.Readers.CMSBReaders import CMSBReader
import config as cf


targets = [['1', '1', '1'],
           ['2', '2', '0']]
months = ['2014-2', '2014-3']

reader = CMSBReader(targets, months, cf.loanDir, cf.transDir, cf.prodDir, cf.fieldName2fieldType)
reader.read()
