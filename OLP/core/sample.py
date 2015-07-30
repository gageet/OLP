class Sample(object):

    def __init__(self, cust_num=0, protol_nums=[], X=[], y=0, y_pred=0):
        self._cust_num = cust_num
        self._protol_nums = protol_nums
        self._X = X
        self._y = y
        self._y_pred = y_pred

    def get_X(self):
        return self._X

    def set_X(self, X):
        self._X = X

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_y_pred(self, y_pred):
        return self._y_pred

    def set_y_pred(self, y_pred):
        self._y_pred = y_pred


class Samples(list):

    def __init__(self, field_indexes):
        self._field_indexes = field_indexes

    def add(self, sample):
        self.append(sample)

    def get_Xs(self):
        Xs = []
        for sample in self:
            Xs.append(sample.get_X())
        return Xs

    def get_ys(self):
        ys = []
        for sample in self:
            ys.append(sample.get_y())
        return ys

    def save(self, filename):
        print 'save in', filename
