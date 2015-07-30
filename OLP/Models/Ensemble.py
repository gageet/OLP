from OLP.Models.Classifier import Classifier
from sklearn import ensemble


class AdaBoostClassifier(Classifier):

    def __init__(self, nEstimators=100):
        Classifier.__init__(self)
        self.clf = ensemble.AdaBoostClassifier(n_estimators=nEstimators)


class RandomForestClassifier(Classifier):

    def __init__(self, nEstimators=100):
        Classifier.__init__(self)
        self.clf = ensemble.RandomForestClassifier(n_estimators=nEstimators)

    def getFeatImportances(self):
        return self.clf.feature_importances_
