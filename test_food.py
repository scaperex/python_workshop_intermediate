from unittest import TestCase
from testing import food


class TestFood(TestCase):
    def test___str__(self):
        myFood = food('banana')
        self.assertIsInstance(myFood,int,msg=1)
        # self.assertEqual(1, 2, msg="hi")
