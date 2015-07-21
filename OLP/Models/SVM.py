from sklearn import preprocessing
from sklearn import svm
from OLP.Models.Classifier import Classifier


class SVM(Classifier):

    def __init__(self, C=1.0, kernel='rbf', gamma=0.0, tol=0.001, classWeight=None, maxIter=-1):
        Classifier.__init__(self)
        self.scaler = preprocessing.MinMaxScaler()
        self.clf = svm.SVC(C=C, kernel=kernel, gamma=gamma, tol=tol, class_weight=classWeight, max_iter=maxIter)

    def fit(self, xs, ys):
        xsScaled = self.scaler.fit_transform(xs)
        self.clf.fit(xsScaled, ys)

    def predict(self, xs):
        xsScaled = self.scaler.transform(xs)
        ys = self.clf.predict(xsScaled)
        return ys
