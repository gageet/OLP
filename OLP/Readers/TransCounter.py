# coding: utf-8

import CounterConfig
import math
from ReaderTools import UniPrinter

class TransCounter:
    '''
    将输入的交易信息表进行统计，得到每个key想要得到的间接属性，生成交易信息特征表。计算规则写在CountConfig.py配置文件中
    '''

    def __init__(self,table):
        '''
        :param table: 要处理的交易信息表，格式（{title:index,title2:index2,……}{key:[[a1,a2……][b1,b2……]，……]}）
        '''
        self.title2index = table[0]
        self.tableContent = table[1]
        self.indiTitle2index = {}
        i = 0
        for propKey in CounterConfig.countRules:
            self.indiTitle2index[propKey] = i
            i += 1
        self.resultDict = {}

    def countProp(self):
        '''
        处理交易信息表
        :return:处理好的交易信息表，格式（{title:index,title2:index2,……}{key:[proA,proB,……}）
        '''
        for loanKey in self.tableContent:
            value = []
            for propKey in CounterConfig.countRules:
                calcResult = self.calcProp(self.tableContent[loanKey], CounterConfig.countRules[propKey])
                value.append(calcResult)
            self.resultDict[loanKey] = value
        return self.indiTitle2index, self.resultDict

    def calcProp(self, loan, prop):
        '''
        得到某个客户信息的某条间接属性
        :param loan: 某条客户的所有交易记录
        :param prop: 配置信息中要统计的某条间接属性
        :return:
        '''
        sum, count = 0.0, 0
        formula = prop['formula']
        title = prop['title']
        rules = prop['rules']

        addedElement = []
        for i in range(len(loan[0])):
            ruleFlag = True
            for ruleKey in rules:
                if not rules[ruleKey] == loan[self.title2index[ruleKey]][i]:
                    ruleFlag = False

            if ruleFlag:
                addedElement.append(float(loan[self.title2index[title]][i]))

        result = formula(addedElement)
        if math.isnan(result):
            result = 0
        return result