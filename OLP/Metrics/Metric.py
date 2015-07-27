class Metric(object):

    @classmethod
    def get(cls, ysTrue, ysPred):
        raise NotImplementedError

    @classmethod
    def format(cls, metric):
        raise NotImplementedError


class FltMetric(Metric):

    @classmethod
    def format(cls, metric):
        return '%s = %.4f' % (cls.__name__, metric)


def getMetric(name):
    modName, clsName = name.rsplit('.', 1)
    mod = __import__(modName, globals(), locals(), [clsName], -1)
    cls = getattr(mod, clsName)
    return cls
