class FieldFilter(object):

    def filter(self, fields):
        raise NotImplementedError


class FieldConvertor(object):

    def convert(self, fields):
        raise NotImplementedError


class Reader(object):

    def read(self):
        raise NotImplementedError
