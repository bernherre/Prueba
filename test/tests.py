# coding=UTF-8

import unittest
import sys

sys.path.insert(1, '../')
from __init__ import op


import unittest
class TestOp(unittest.TestCase):

    def test_op_int(self):
        self.assertEqual(op.int(4, 2, 1), 8, "Should be 8")

if __name__ == '__main__':
    unittest.main()

