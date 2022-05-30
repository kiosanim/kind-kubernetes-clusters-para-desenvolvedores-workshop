import unittest
from test_fake_prospects_api import TestFakeProspectsAPI
from test_fake_prospects_controller import TestFakeProspectsController
from test_fake_prospects_service import TestFakeProspectsService


def suite_all_test_cases():
    suite = unittest.TestSuite()
    suite.addTest(TestFakeProspectsAPI)
    suite.addTest(TestFakeProspectsService)
    suite.addTest(TestFakeProspectsController)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_all_test_cases())
