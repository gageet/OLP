# coding: utf-8

import sys
from OLP.Readers.CMSBReaders import CMSBLoanReader, CMSBTransReader


def testCMSBLoanReader():
    filenames = sys.argv[1:]
    reader = CMSBLoanReader(filenames, '协议号')
    title2index, loans = reader.read()
    print title2index
    print loans


def testCMSBTransReader():
    filenames = sys.argv[1:]
    reader = CMSBTransReader(filenames, '我行客户号')
    title2index, transs = reader.read()
    print title2index
    print transs


if __name__ == '__main__':

    testCMSBTransReader()
