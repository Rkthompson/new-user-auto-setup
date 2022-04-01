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
from new_user_auto_setup import new_user_request

"""

"Arrange-Act-Assert"

a pattern for arranging and formatting code in UnitTest methods:

Each method should group these functional sections, separated by blank lines:

Arrange all necessary preconditions and inputs.
Act on the object or method under test.
Assert that the expected results have occurred.

"""


class TestNewUserRequest(unittest.TestCase):
    pass


print("######################## This is running from ########################")
print(sys.path)
print("######################################################################")


if __name__ == '__main__':
    unittest.main()
