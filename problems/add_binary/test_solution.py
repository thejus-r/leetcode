import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution("11","1"), "100")

    def test_case2(self):
        self.assertEqual(solution("1010","1011"), "10101")

    def test_case3(self):
        self.assertEqual(solution("1010","0"), "1010")

    def test_case4(self):
        self.assertEqual(solution("0","1011"), "1011")

if __name__ == '__main__':
    unittest.main()