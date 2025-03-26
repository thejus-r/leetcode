import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution([1,3], [2]), 2)

    def test_case2(self):
        self.assertEqual(solution([1,2], [3,4]), 2.5)

if __name__ == '__main__':
    unittest.main()
