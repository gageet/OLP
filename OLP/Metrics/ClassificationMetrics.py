from sklearn import metrics


def getAccuracy(ysTrue, ysPred):
    return metrics.accuracy_score(ysTrue, ysPred)


def getPrecision(ysTrue, ysPred):
    return metrics.precision_score(ysTrue, ysPred)


def getRecall(ysTrue, ysPred):
    return metrics.recall_score(ysTrue, ysPred)


def getF1(ysTrue, ysPred):
    return metrics.f1_score(ysTrue, ysPred)


def getAUC(ysTrue, ysPred):
    return metrics.roc_auc_score(ysTrue, ysPred)


def getConfusionMatrix(ysTrue, ysPred):
    return metrics.confusion_matrix(ysTrue, ysPred)
