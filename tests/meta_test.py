import json


__author__ = 'Timothy S. Jones <jonests@bu.edu>, Densmore Lab, BU'
__license__ = 'GPL3'


def get_json_file_contents(file_name):
    with open(file_name) as f:
        obj = json.load(f)
    return obj


def get_normative_json(file_name):
    obj = get_json_file_contents(file_name)
    normative = {}
    for coll in obj:
        if coll["collection"] not in normative:
            normative[coll["collection"]] = []
        normative[coll["collection"]].append(coll)
    return normative


def ref_obj_exists(j, coll, name):
    b = False
    for dst in j[coll]:
        if dst["name"] == name:
            b = True
            break
    return b


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
