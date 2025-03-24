def solution(dividend: int, divisor: int) -> int:
    if dividend == divisor: return 1
    sign = 1
    if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
        sign = -1

    n = abs(dividend)
    d = abs(divisor)
    qoutient = 0
    while(n >= d):
        count = 0
        while(n >= (d << (count + 1))):
            count += 1
        qoutient += 1 << count
        n -= d << count

    if (sign == 1 and qoutient >= 1<<31):
        return (1<<31) - 1
    
    if (sign == -1 and qoutient >= 1<<31):
        return sign * 1<<31

    return sign * qoutient

res = solution(-2147483648, -1)
print(res, (1<<31)-1)
