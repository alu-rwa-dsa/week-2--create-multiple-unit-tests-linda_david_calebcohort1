import unittest
from question9 import array_dif

class Test_arrayDif(unittest.TestCase):
    
    def test_array_dif(self):

        self.assertEqual(array_dif([8,1,3],[8,1,2,3]),{2})
        
    def test_array_dif_error(self):

        self.assertRaises(TypeError ,lambda:array_dif([8,1,3,5,9,78],[8,1,2,3]))

if __name__ == "__main__":
    unittest.main()