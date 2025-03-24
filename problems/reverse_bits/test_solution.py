import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution(43261596), 964176192)

    def test_case2(self):
        self.assertEqual(solution(4294967293), 3221225471)


if __name__ == '__main__':
    unittest.main()