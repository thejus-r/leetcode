import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution(10,3), 3)

    def test_case2(self):
        self.assertEqual(solution(7,-3), -2)

    def test_case3(self):
        self.assertEqual(solution(7,7), 1)

    def test_case4(self):
        self.assertEqual(solution(-2147483648,-1), 2147483647)

if __name__ == '__main__':
    unittest.main()