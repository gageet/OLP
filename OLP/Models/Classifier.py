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
