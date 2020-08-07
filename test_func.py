from unittest import TestCase
from testing import func

class TestFunction(TestCase):
    def test_function(self):
        self.assertEqual(func(1), 2)
    def test_function1(self):
        self.assertEqual(func(-1), 0)
    def test_function2(self):
        self.assertGreater(func(1111111), 0)