def addBinary(a: str, b: str) -> str:

    lenA = len(a)
    lenB = len(b)

    res = ""

    # keeping 'a' always bigger
    if lenB > lenA:
        a, b = b, a
        lenA, lenB = lenB, lenA
  
    idxA, idxB = lenA-1, lenB-1

    carry = "0"
    while(idxA > 0):
        if(a[idxA] == "1" and b[idx] == "1"):
            carry = "1"


    return res

# driver code
res = addBinary("11", "1")
print(res)
