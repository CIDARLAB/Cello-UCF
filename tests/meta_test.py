__author__ = 'Timothy S. Jones <jonests@bu.edu>, Densmore Lab, BU'
__license__ = 'GPL3'


class TestFileMeta(type):
    def __new__(cls, name, bases, attrs):
        def create_func(test_name, f):
            def func(self):
                self.check_file(f)
            func.__name__ = "test_" + str(test_name)
            return func

        args = attrs['get_test_args']
        for test_name, f in args():
            func = create_func(test_name, f)
            attrs[func.__name__] = func

        return type.__new__(cls, name, bases, attrs)
