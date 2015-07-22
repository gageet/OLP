from OLP.Models.SVM import SVM


if __name__ == '__main__':

    xs = [[-1., -1.], [-2., -1.], [1., 1.], [2., 1.]]
    ys = [1, 1, 2, 2]
    clf = SVM()
    clf.fit(xs, ys)
    print clf.predict([[-0.8, -1]])
