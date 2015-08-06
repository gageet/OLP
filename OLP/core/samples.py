# -*- coding: utf-8 -*-

import numpy as np
import xmltodict


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
            xml = infile.read()
            d = xmltodict.parse(xml)
            for i, s in enumerate(d['samples']['sample']):
                cust_num = s['cust_num']
                protol_nums = s['protol_nums']
                y = int(s['y'])
                y_pred = int(s['y_pred'])
                X = []
                for j, x in enumerate(s['X']['x']):
                    val = float(x['val'])
                    X.append(val)
                    if i == 0:  # 构建索引
                        name = x['name'].encode('utf-8')
                        self._x_indexes[name] = j
                sample = Sample(cust_num, protol_nums, X, y, y_pred)
                self.append(sample)

    def save(self, filename):
        d = {'samples': {'sample': []}}
        for sample in self:
            s = {}
            s['cust_num'] = sample.get_cust_num()
            s['protol_nums'] = {'protol_num': sample.get_protol_nums()}
            s['y'] = sample.get_y()
            s['y_pred'] = sample.get_y_pred()
            s['X'] = {'x': []}
            X = sample.get_X()
            for name, index in self._x_indexes.iteritems():
                s['X']['x'].append({'val': str(X[index]), '@name': name.decode('utf-8')})
            d['samples']['sample'].append(s)
        xml = xmltodict.unparse(d, pretty=True).encode('utf-8')

        with open(filename, 'w') as outfile:
            outfile.write(xml)
