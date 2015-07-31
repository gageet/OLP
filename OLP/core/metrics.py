from sklearn import metrics


class Metric(object):

    @classmethod
    def get(cls, ys, ys_pred):
        raise NotImplementedError

    @classmethod
    def format(cls, metric):
        raise NotImplementedError


class FltMetric(Metric):

    @classmethod
    def format(cls, metric):
        return '%s = %.4f' % (cls.__name__, metric)


class Accuracy(FltMetric):

    @classmethod
    def get(cls, ys, ys_pred):
        return metrics.accuracy_score(ys, ys_pred)


class Precision(FltMetric):

    @classmethod
    def get(cls, ys, ys_pred):
        return metrics.precision_score(ys, ys_pred)


class Recall(FltMetric):

    @classmethod
    def get(cls, ys, ys_pred):
        return metrics.recall_score(ys, ys_pred)


class F1(FltMetric):

    @classmethod
    def get(cls, ys, ys_pred):
        return metrics.f1_score(ys, ys_pred)


class AUC(FltMetric):

    @classmethod
    def get(cls, ys, ys_pred):
        return metrics.roc_auc_score(ys, ys_pred)


def get_metric(name):
    modname, clsname = name.rsplit('.', 1)
    mod = __import__(modname, globals(), locals(), [clsname], -1)
    cls = getattr(mod, clsname)
    return cls
