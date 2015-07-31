from sklearn import preprocessing
from sklearn import svm
from sklearn import ensemble
from sklearn.externals import joblib


class Classifier(object):

    def __init__(self):
        self.clf = None

    def fit(self, xs, ys):
        self.clf.fit(xs, ys)

    def predict(self, xs):
        ys = self.clf.predict(xs)
        return ys

    def save(self, filename):
        joblib.dump(self.clf, filename)

    def load(self, filename):
        self.clf = joblib.load(filename)


class SVM(Classifier):

    def __init__(self, C=1.0, kernel='rbf', gamma=0.0, tol=0.001, class_weight=None, max_iter=-1):
        Classifier.__init__(self)
        self.scaler = preprocessing.MinMaxScaler()
        self.clf = svm.SVC(C=C, kernel=kernel, gamma=gamma, tol=tol, class_weight=class_weight, max_iter=max_iter)

    def fit(self, xs, ys):
        xs_scaled = self.scaler.fit_transform(xs)
        self.clf.fit(xs_scaled, ys)

    def predict(self, xs):
        xs_scaled = self.scaler.transform(xs)
        ys = self.clf.predict(xs_scaled)
        return ys


class AdaBoostClassifier(Classifier):

    def __init__(self, n_estimators=100):
        Classifier.__init__(self)
        self.clf = ensemble.AdaBoostClassifier(n_estimators=n_estimators)


class RandomForestClassifier(Classifier):

    def __init__(self, n_estimators=100):
        Classifier.__init__(self)
        self.clf = ensemble.RandomForestClassifier(n_estimators=n_estimators)

    def get_x_importances(self):
        return self.clf.feature_importances_


def get_classifier(name, param):
    modname, clsname = name.rsplit('.', 1)
    mod = __import__(modname, globals(), locals(), [clsname], -1)
    cls = getattr(mod, clsname)
    clf = cls(**param)
    return clf
