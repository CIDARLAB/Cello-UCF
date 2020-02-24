import unittest
import json
import jsonschema
from glob import glob
from os import getcwd
from os.path import basename
from .meta_test import TestFileMeta


__author__ = 'Timothy S. Jones <jonests@bu.edu>, Densmore Lab, BU'
__license__ = 'GPL3'


class TestUCFs(unittest.TestCase, metaclass=TestFileMeta):

    def get_test_args():
        files = glob("files/v2/ucf/**/*.UCF.json", recursive=True)
        for f in files:
            yield (basename(f), f)

    def check_file(self, f):
        with open("schema/v2/ucf.schema.json") as schema_file:
            schema = json.load(schema_file)
        resolver = jsonschema.RefResolver("file://" + getcwd() + "/schema/v2/", "")
        validator = jsonschema.Draft7Validator(schema, resolver=resolver)
        with open(f) as ucf_file:
            ucf = json.load(ucf_file)
        validator.validate(ucf)


if __name__ == '__main__':
    unittest.main()
