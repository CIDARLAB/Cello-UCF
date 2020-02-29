import unittest
import json
import jsonschema
from glob import glob
from os import getcwd
from os.path import basename
from .meta_test import TestFileMeta


__author__ = 'Timothy S. Jones <jonests@bu.edu>, Densmore Lab, BU'
__license__ = 'GPL3'


def get_file_contents(file_name):
    with open(file_name) as f:
        obj = json.load(f)
    return obj


def get_normative_json(file_name):
    obj = get_file_contents(file_name)
    normative = {}
    for coll in obj:
        if coll["collection"] not in normative:
            normative[coll["collection"]] = []
        normative[coll["collection"]].append(coll)
    return normative


class TestUserConstraintsFileSyntax(unittest.TestCase, metaclass=TestFileMeta):

    def get_test_args():
        files = glob("files/v2/ucf/**/*.UCF.json", recursive=True)
        for f in files:
            yield (basename(f), f)

    def _test_syntax(self, f):
        with open("schemas/v2/ucf.schema.json") as schema_file:
            schema = json.load(schema_file)
        resolver = jsonschema.RefResolver("file://" + getcwd() + "/schemas/v2/", "")
        validator = jsonschema.Draft7Validator(schema, resolver=resolver)
        with open(f) as ucf_file:
            ucf = json.load(ucf_file)
        validator.validate(ucf)


class TestUserConstraintsFileStructure(unittest.TestCase, metaclass=TestFileMeta):

    def get_test_args():
        files = glob("files/v2/ucf/**/*.UCF.json", recursive=True)
        for f in files:
            yield (basename(f), f)

    def ref_obj_exists(self, j, coll, name):
        b = False
        for dst in j[coll]:
            if dst["name"] == name:
                b = True
                break
        self.assertTrue(b, msg="{} missing from file.".format(name))
        
    def _test_gate_models_exist(self, f):
        j = get_normative_json(f)
        for gate in j["gates"]:
            self.ref_obj_exists(j, "models", gate["model"])

    def _test_gate_structures_exist(self, f):
        j = get_normative_json(f)
        for gate in j["gates"]:
            self.ref_obj_exists(j, "structures", gate["structure"])

    def _test_model_functions_exist(self, f):
        j = get_normative_json(f)
        for model in j["models"]:
            for function in model["functions"]:
                self.ref_obj_exists(j, "functions", model["functions"][function])


if __name__ == '__main__':
    unittest.main()
