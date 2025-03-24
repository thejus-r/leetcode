import unittest
from solution import add

class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(add(2,4), 6)

if __name__ == '__main__':
    unittest.main()