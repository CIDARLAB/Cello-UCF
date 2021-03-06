import unittest
import json
import jsonschema
from glob import glob
from os import getcwd
from os.path import basename
from .meta_test import TestFileMeta, get_json_file_contents, get_normative_json, ref_obj_exists


__author__ = 'Timothy S. Jones <jonests@bu.edu>, Densmore Lab, BU'
__license__ = 'GPL3'


class TestInputSensorFileSyntax(unittest.TestCase, metaclass=TestFileMeta):

    def get_test_args():
        files = glob("files/v2/input/**/*.input.json", recursive=True)
        for f in files:
            yield (basename(f), f)

    def _test_syntax(self, f):
        schema = get_json_file_contents("schemas/v2/input_sensor_file.schema.json")
        resolver = jsonschema.RefResolver("file://" + getcwd() + "/schemas/v2/", "")
        validator = jsonschema.Draft7Validator(schema, resolver=resolver)
        with open(f) as isf_file:
            isf = json.load(isf_file)
        validator.validate(isf)


class TestInputSensorFileStructure(unittest.TestCase, metaclass=TestFileMeta):

    def get_test_args():
        files = glob("files/v2/input/**/*.input.json", recursive=True)
        for f in files:
            yield (basename(f), f)

    def _test_sensor_models_exist(self, f):
        j = get_normative_json(f)
        for gate in j["input_sensors"]:
            name = gate["model"]
            b = ref_obj_exists(j, "models", name)
            self.assertTrue(b, msg="{} missing from file.".format(name))

    def _test_sensor_structures_exist(self, f):
        j = get_normative_json(f)
        for gate in j["input_sensors"]:
            name = gate["structure"]
            b = ref_obj_exists(j, "structures", name)
            self.assertTrue(b, msg="{} missing from file.".format(name))

    def _test_model_functions_exist(self, f):
        j = get_normative_json(f)
        for model in j["models"]:
            for function in model["functions"]:
                name = model["functions"][function]
                b = ref_obj_exists(j, "functions", name)
                self.assertTrue(b, msg="{} missing from file.".format(name))

    def _test_output_parts_exist(self, f):
        j = get_normative_json(f)
        for structure in j["structures"]:
            for output in structure["outputs"]:
                b = ref_obj_exists(j, "parts", output)
                self.assertTrue(b, msg="{} missing from file.".format(output))


if __name__ == '__main__':
    unittest.main()
