# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

# Example 1:

# Input: x = 4
# Output: 2


class Solution:

    def mySqrt(self, x: int):
        if x==0 or x==1:
            return x
        if x==2 or x==3:
            return 1
        def square(val):

            return val*val
        
        l=2
        r=x//2+1

        while l<r:

            mid = l+(r-l)//2
            if square(mid)<=x:
                l = mid+1
            elif square(mid)>x:
                r = mid
        return l-1
    x=int(input("Enter number:"))
    print(mySqrt(1,x))

a=Solution()
