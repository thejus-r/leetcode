# Leetcode 8: String to Integer (atoi)
# tags: String

def myAtoi(s: str) -> int:
    if len(s) == 0:
        return 0
   
    num = 0
    sign = 1
    i = 0

    while (i < len(s)):
        if (s[i] == ' '):
            i += 1
        else:
            break

    if (i < len(s)) and (s[i] == '-' or s[i] == '+'):
        sign = -1
        i += 1

    print(s[i])
    print(sign)
    while(i < len(s)):
        if(ord(s[i]) >= 48 and ord(s[i]) < 58):
            num = (num * 10) + int(s[i])
            if num >= 2**31:
                if sign == 1:
                    return (2**31) - 1
                else:
                    return -(2**31)
            i += 1
        else:
            break

    return sign * num

# driver code
res = myAtoi("-8014081204809128409")
print("Final Result: ", res)

