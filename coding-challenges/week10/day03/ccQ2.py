def Numberof1Bits(n):
    res = 0
    while n:
        res += n & 1
        n >>= 1

    return res

n = input()
ans = Numberof1Bits(n)
print(ans)