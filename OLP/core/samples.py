# -*- coding: utf-8 -*-

import numpy as np


class Sample(object):

    def __init__(self, cust_num=0, protol_nums=[], X=[], y=0, y_pred=0):
        self._cust_num = cust_num
        self._protol_nums = protol_nums
        self._X = X
        self._y = y
        self._y_pred = y_pred

    def __repr__(self):
        s = 'Sample:\n\tcust_num = %s\n\tprotol_nums = %s\n\tX = %s\n\ty = %d\n\ty_pred = %d' %\
                (self._cust_num, str(self._protol_nums), str(self._X), self._y, self._y_pred)
        return s

    def get_cust_num(self):
        return self._cust_num

    def set_cust_num(self, cust_num):
        self._cust_num = cust_num

    def get_protol_nums(self):
        return self._protol_nums

    def set_protol_nums(self, protol_nums):
        self._protol_nums = protol_nums

    def get_x(self, index):
        return self._X[index]

    def set_x(self, index, x):
        self._X[index] = x

    def get_X(self):
        return self._X

    def set_X(self, X):
        self._X = X

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_y_pred(self):
        return self._y_pred

    def set_y_pred(self, y_pred):
        self._y_pred = y_pred


class Samples(list):

    def __init__(self, x_indexes={}, samples=[]):
        list.__init__(self)
        self._x_indexes = x_indexes
        self.extend(samples)

    def __repr__(self):
        s = '\n'.join([repr(sample) for sample in self])
        return s

    def get_x_indexes(self):
        return self._x_indexes

    def get_Xs(self):
        Xs = []
        for sample in self:
            Xs.append(sample.get_X())
        return Xs

    def get_avg_X(self):
        Xs = self.get_Xs()
        avg_X = np.mean(Xs, axis=0)
        return avg_X

    def get_std_X(self):
        Xs = self.get_Xs()
        std_X = np.std(Xs, axis=0)
        return std_X

    def get_ys(self):
        ys = []
        for sample in self:
            ys.append(sample.get_y())
        return ys

    def get_ys_pred(self):
        ys_pred = []
        for sample in self:
            ys_pred.append(sample.get_y_pred())
        return ys_pred

    def clear(self):
        self._x_indexes.clear()
        del self[:]

    def load(self, filename):
        self.clear()
        with open(filename) as infile:
            # 读取第一行
            firstline = infile.readline()
            fields = firstline.strip().split('\t')
            for index, name in enumerate(fields[4:]):
                self._x_indexes[name] = index

            for line in infile:
                fields = line.strip().split('\t')
                y_pred = int(fields[0])
                y = int(fields[1])
                cust_num = fields[2]
                protol_nums = fields[3].split(',')
                X = [float(x) for x in fields[4:]]
                sample = Sample(cust_num, protol_nums, X, y, y_pred)
                self.append(sample)

    def save(self, filename):
        with open(filename, 'w') as outfile:
            items = self._x_indexes.items()
            outfile.write('\t'.join(['是否逾期(预测)', '是否逾期(实际)', '客户号', '协议号'] + [item[0] for item in items]))
            outfile.write('\n')

            for sample in self:
                cust_num = sample.get_cust_num()
                protol_nums = sample.get_protol_nums()
                X = sample.get_X()
                y = sample.get_y()
                y_pred = sample.get_y_pred()
                strlist = [str(y_pred), str(y), cust_num]
                strlist.append(','.join(protol_nums))
                for item in items:
                    index = item[1]
                    strlist.append(str(X[index]))
                outfile.write('\t'.join(strlist))
                outfile.write('\n')
