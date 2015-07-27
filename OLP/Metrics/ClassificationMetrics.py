from OLP.Metrics.Metric import FltMetric
from sklearn import metrics


class Accuracy(FltMetric):

    @classmethod
    def get(cls, ysTrue, ysPred):
        return metrics.accuracy_score(ysTrue, ysPred)


class Precision(FltMetric):

    @classmethod
    def get(cls, ysTrue, ysPred):
        return metrics.precision_score(ysTrue, ysPred)


class Recall(FltMetric):

    @classmethod
    def get(cls, ysTrue, ysPred):
        return metrics.recall_score(ysTrue, ysPred)


class F1(FltMetric):

    @classmethod
    def get(cls, ysTrue, ysPred):
        return metrics.f1_score(ysTrue, ysPred)


class AUC(FltMetric):

    @classmethod
    def get(cls, ysTrue, ysPred):
        return metrics.roc_auc_score(ysTrue, ysPred)
