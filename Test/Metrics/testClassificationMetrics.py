from OLP.Models.SVM import SVM
from OLP.Metrics.ClassificationMetrics import *


if __name__ == '__main__':

    xs = [[-1., -1.], [-2., -1.], [1., 1.], [2., 1.]]
    ys = [0, 0, 1, 1]
    clf = SVM()
    clf.fit(xs, ys)
    ysTrue = [0, 0, 1, 1]
    ysPred = clf.predict([[-0.8, -1], [-0.7, 0.6], [0.9, 0.9], [-0.8, -0.8]])

    print 'accuracy =', getAccuracy(ysTrue, ysPred)
    print 'precision =', getPrecision(ysTrue, ysPred)
    print 'recall =', getRecall(ysTrue, ysPred)
    print 'f1 =', getF1(ysTrue, ysPred)
    print 'auc =', getAUC(ysTrue, ysPred)
    print 'confusion matrix =\n', getConfusionMatrix(ysTrue, ysPred)
