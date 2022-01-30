import unittest

import os
import sys
import pathlib

this_folder = pathlib.Path(__file__).parent.resolve()
package_folder = os.path.join(os.path.dirname(this_folder), 'dev')
sys.path.append(package_folder)

#---------------------------------------------------- 

from Pointer import Point

class TestMain(unittest.TestCase):
    """
assertEqual(a,b)           a==b
assertNotEqual(a,b)        a!=b
assertTrue(x)	           bool(x) is True
assertFalse(x)	           bool(x) is False
assertIs(a,b)	           a is b
assertIs(a,b)	           a is b
assertIsNot(a, b)          a is not b
assertIsNone(x)	           x is None
assertIsNotNone(x)         x is not None
assertIn(a, b)	           a in b
assertNotIn(a, b)          a not in b
assertIsInstance(a, b)     isinstance(a, b)
assertNotIsInstance(a, b)  not isinstance(a, b)

    To execute:
    >python -m unittest -v main_test.TestMain
    """
    def test__init_basic(self):
        """
        Any method name starting with test_ will be executed. I prefer test__<methodname>_<opname>
        """
        p = Point(-1,1)
        expected = 2
        self.assertEqual(p.quad(), expected)

    def test__init_basic_negative(self):
        p = Point(-1,1)
        expected = 3
        self.assertNotEqual(p.quad(), expected)

    def test__add(self):
        p1 = Point(1,1)
        p2 = Point(-1,-1)
        p3 = p1.add(p2)
        self.assertEqual(p3.x, 0)
        self.assertEqual(p3.y, 0)
        self.assertEqual(p3.quad(), 1)

    def test__sub(self):
        p1 = Point(3,3)
        p2 = Point(1,1)
        p3 = p1.sub(p2)
        self.assertEqual(p3.x, 2)
        self.assertEqual(p3.y, 2)
        self.assertEqual(p3.quad(), 1)

    def test__mul(self):
        """
        Yes! you can write test for a non-existing method.
        This is basically test driven development
        """
        p1 = Point(3,3)
        p2 = Point(1,1)
        """
        # uncomment this block to see the test failing
        p3 = p1.mul(p2)
        self.assertEqual(p3.x, 3)
        self.assertEqual(p3.y, 3)
        self.assertEqual(p3.quad(), 1)
        """



#---------------------------------------------------- 
if __name__ == "__main__":
    print(TestMain.__doc__)
    unittest.main()