'''
Created on 17-Jul-2018

@author: anitr
'''
import unittest
from random import random
from Test3 import bubbleSort
class Test(unittest.TestCase):
        def test_bubble_sort(self):
            seq = [random() for _ in Test3.alist]
            sorted_seq = sorted(seq)
            self.assertEqual(bubbleSort(seq), sorted_seq)
