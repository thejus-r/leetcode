import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution("(()"), 2)

    def test_case2(self):
        self.assertEqual(solution(")()())"), 4)

    def test_case3(self):
        self.assertEqual(solution(""), 0)

    def test_case4(self):
        self.assertEqual(solution("(()(((()"), 2)

if __name__ == '__main__':
    unittest.main()
