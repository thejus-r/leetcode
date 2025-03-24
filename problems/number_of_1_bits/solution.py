def solution(n: int) -> int:
    res = 0
    while n:
        n &= (n - 1)
        res += 1
    return res

res = solution(11)
print("Result: ", res)