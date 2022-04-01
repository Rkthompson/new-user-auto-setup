import unittest

"""

Sibling package imports

A working solution to the error:

ImportError: attempted relative import with no known parent package

    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# from new_user_auto_setup import new_user_request
from new_user_auto_setup.new_user_request import NewUserRequest # noqa

"""

"Arrange-Act-Assert"

a pattern for arranging and formatting code in UnitTest methods:

Each method should group these functional sections, separated by blank lines:

Arrange all necessary preconditions and inputs.
Act on the object or method under test.
Assert that the expected results have occurred.

"""


class TestNewUserRequest(unittest.TestCase):

    def test_new_user_init(self):
        # setup data to populate the test class
        test_name = "John Sample"
        test_job_title = "Test Manager"
        test_division = "Test Division"
        test_department = "Test Department"
        test_model_account_after = "Jane Sample"
        test_need_adobe_cc = True
        test_need_exacqvision = True
        test_need_ftp = True
        test_need_promail = True

        # create an object instance with test values
        this_test_object = NewUserRequest(test_name, test_job_title,
                                          test_division, test_department,
                                          test_model_account_after,
                                          test_need_adobe_cc,
                                          test_need_exacqvision, test_need_ftp,
                                          test_need_promail)

        # check that attributes were succesfully created with values passed
        self.assertEqual(this_test_object.name, test_name)
        self.assertEqual(this_test_object.job_title, test_job_title)
        self.assertEqual(this_test_object.division, test_division)
        self.assertEqual(this_test_object.department, test_department)
        self.assertEqual(this_test_object.model_account_after,
                         test_model_account_after)
        self.assertEqual(this_test_object.need_adobe_cc, test_need_adobe_cc)
        self.assertEqual(this_test_object.need_exacqvision,
                         test_need_exacqvision)
        self.assertEqual(this_test_object.need_ftp, test_need_ftp)
        self.assertEqual(this_test_object.need_promail, test_need_promail)

        # show the sys.path used
        print("############### This test ran from sys.path ##################")
        print(sys.path)
        print("##############################################################")

        # print the object to screen
        print(this_test_object)


if __name__ == '__main__':
    unittest.main()
