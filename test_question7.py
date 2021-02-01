import unittest
from question7 import frequency_counter

class Test_frequency_counter(unittest.TestCase):
    
    def test_frequency_counter(self):
        self.assertEqual(frequency_counter("calebb"),{'c': 1, 'a': 1, 'l': 1, 'e': 1, 'b': 2})
    def test_frequency_counter1(self):
        self.assertEqual(frequency_counter("linda"),{'l': 1, 'i': 1, 'n': 1, 'd': 1, 'a': 1})
    def test_frequency_counter2(self):
        self.assertEqual(frequency_counter("Davidd"),{'D': 1, 'a': 1, 'v': 1, 'i': 1, 'd': 2})

if __name__ == "__main__":
    unittest.main()