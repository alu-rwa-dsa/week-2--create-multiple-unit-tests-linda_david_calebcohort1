import unittest
from question8 import list_combinator

class Test_list_comb(unittest.TestCase):
    
    def test_list_combinator1(self):

        self.assertEqual(list_combinator([[3,4,24,30],[49,30,43]]),{3, 4, 43, 49, 24, 30})
    def test_list_combinator2(self):

        self.assertEqual(list_combinator([[3,4,24,30],[49,30,43]]),{3, 4, 43, 49, 24, 30})

if __name__ == "__main__":
    unittest.main()