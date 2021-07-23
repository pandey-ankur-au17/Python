class Solution:
    def climbStairs(n: int):
        if (n == 1 or n == 2):
            return n
        else:
            a = 1
            b = 2
            for i in range(n-2):
                b += a
                a = b - a
            return b
    n=int(input("Enter the stairs:"))
    print(climbStairs(n))