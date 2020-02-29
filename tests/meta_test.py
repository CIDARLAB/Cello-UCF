__author__ = 'Timothy S. Jones <jonests@bu.edu>, Densmore Lab, BU'
__license__ = 'GPL3'


class TestFileMeta(type):
    def __new__(cls, name, bases, attrs):
        def create_func(test_name, file_name, test_func):
            def func(self):
                test_func(self, file_name)
            func.__name__ = "test_{}_{}".format(str(test_name), attr[6:])
            return func

        args = attrs['get_test_args']
        for test_name, file_name in args():
            d = {}
            for attr in attrs:
                if attr.startswith("_test_"):
                    func = create_func(test_name, file_name, attrs[attr])
                    d[func.__name__] = func
            for key in d:
                attrs[key] = d[key]

        return type.__new__(cls, name, bases, attrs)
