def solution(n: int) -> int:
    res = 0
    for i in range (32):
       bit = (n >> i) & 1
       res = res | (bit << (31 - i)) 

    return int(bin(n)[2:].zfill(32)[::-1], 2)


res = solution(43261596)
print("Result: ", res)