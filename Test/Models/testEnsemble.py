from OLP.Models.Ensemble import AdaBoostClassifier, RandomForestClassifier


def testAdaBoostClassifier():
    xs = [[-1., -1.], [-2., -1.], [1., 1.], [2., 1.]]
    ys = [1, 1, 2, 2]
    clf = AdaBoostClassifier()
    clf.fit(xs, ys)
    print clf.predict([[0., 3.]])


def testRandomForestClassifier():
    xs = [[-1., -1.], [-2., -1.], [1., 1.], [2., 1.]]
    ys = [1, 1, 2, 2]
    clf = RandomForestClassifier()
    clf.fit(xs, ys)
    print clf.predict([[0., 3.]])


if __name__ == '__main__':

    testAdaBoostClassifier()
    testRandomForestClassifier()
