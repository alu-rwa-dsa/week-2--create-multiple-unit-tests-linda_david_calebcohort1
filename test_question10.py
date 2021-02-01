import unittest
from question10 import number_display

class Test_display(unittest.TestCase):
    
    def test_number_display_1(self):
        
        self.assertEqual(number_display(8),[1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7])

    def test_number_display_error(self):

        self.assertRaises(ValueError, lambda:number_display(1))

        
    
if __name__ =="__main__":
    unittest.main()