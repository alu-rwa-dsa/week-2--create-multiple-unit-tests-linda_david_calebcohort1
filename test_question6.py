import unittest
from question6 import whitesp_remove

class test_whiteSpace(unittest.TestCase):
    
    def test_whitesp_remove(self):
        self.assertEqual(whitesp_remove("Group 2     likes Data Structures and       Algorithms"), "Group 2 likes Data Structures and Algorithms")
    def test_whitesp_remove1(self):
        self.assertEqual(whitesp_remove("Group 2           Algorithms               "),"Group 2 Algorithms")
    def test_whitesp_remove2(self):
        self.assertEqual(whitesp_remove("          Group 2     likes  "),"Group 2 likes")

if __name__ == '__main__':
    unittest.main()