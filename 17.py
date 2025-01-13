# Leetcode 17: Letter Combinations of a Phone Number

from typing import List

def letterCombinations(digits: str) -> List[str]:

    res = []
    keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            }

    def backtrack(i, currStr):
        if (len(currStr) == len(digits)):
            res.append(currStr)
            return

        for c in keypad[digits[i]]:
            backtrack(i + 1, currStr + c)

    if digits:
        backtrack(0, "")
    return res

res = letterCombinations("23")
print("Final Result: ", res)

