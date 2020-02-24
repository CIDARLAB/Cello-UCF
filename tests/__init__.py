from .test_schemas import TestSchemas
from .test_ucfs import TestUCFs
import unittest


__author__ = 'Timothy S. Jones <jonests@bu.edu>, Densmore Lab, BU'
__license__ = 'GPL3'


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for test_case in (TestSchemas, TestUCFs):
        tests = loader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite
