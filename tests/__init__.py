from .test_schemas import TestSchemas
from .test_ucfs import TestUCFs
from .test_input_sensor_files import TestInputSensorFiles
from .test_output_device_files import TestOutputDeviceFiles
import unittest


__author__ = 'Timothy S. Jones <jonests@bu.edu>, Densmore Lab, BU'
__license__ = 'GPL3'


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for test_case in (TestSchemas, TestUCFs):
        tests = loader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite
