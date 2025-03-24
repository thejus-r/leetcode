import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution(11), 3)

    def test_case2(self):
        self.assertEqual(solution(128), 1)

    def test_case3(self):
        self.assertEqual(solution(2147483645), 30)

if __name__ == '__main__':
    unittest.main()