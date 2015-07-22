# coding: utf-8

import sys
from OLP.Readers.CMSBReaders import CMSBLoanReader


if __name__ == '__main__':

    filenames = sys.argv[1:]
    reader = CMSBLoanReader(filenames, '协议号')
    title2index, loans = reader.read()
    print title2index
    print loans
