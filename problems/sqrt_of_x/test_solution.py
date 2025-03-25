import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution(4), 2)

    def test_case2(self):
        self.assertEqual(solution(8), 2)


if __name__ == '__main__':
    unittest.main()
