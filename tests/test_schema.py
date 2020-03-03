import unittest
import json
import jsonschema
from glob import glob
from os.path import basename
from .meta_test import TestFileMeta, get_json_file_contents


__author__ = 'Timothy S. Jones <jonests@bu.edu>, Densmore Lab, BU'
__license__ = 'GPL3'


class TestSchema(unittest.TestCase, metaclass=TestFileMeta):

    def get_test_args():
        files = glob("schemas/**/*.schema.json", recursive=True)
        for f in files:
            yield (basename(f), f)

    def _test_schema(self, f):
        schema = get_json_file_contents(f)
        validator = jsonschema.Draft7Validator(schema)
        validator.check_schema(schema)


if __name__ == '__main__':
    unittest.main()
