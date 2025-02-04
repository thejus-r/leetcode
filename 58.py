# Leetcode 58: Length of the Last Word

def lengthOfLastWord(s: str) -> int:
    res = s.split(" ")
    print(res)
    l = len(res)
    if l == 1:
        return len(res[0])
    else:
        while(l > 3):
            if len(res[l-1]) != 0:
                return len(res[l-1])
            l -= 1

    return 0

#driver code
res = lengthOfLastWord("a ")
print(res)
