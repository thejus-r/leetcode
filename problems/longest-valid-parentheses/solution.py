def solution(s: str) -> int:
    if len(s) == 1:
        return 1
    # When length is non zero
    
    left = right = max_len = 0
    i = 0
    while(i < len(s)):
        if s[i] == "(":
            left += 1
        else:
            right += 1

        if left == right:
            max_len = max(max_len, left + right)
        elif right > left:
            right = left = 0

        i += 1


    left = right = 0
    i = len(s) - 1
    while(i >= 0):
        if s[i] == "(":
            left += 1
        else:
            right += 1

        if left == right:
            max_len = max(max_len, left + right)
        elif left > right:
            right = left = 0

        i -= 1

    return max_len

res = solution(")()()")
print("Result : ", res)
