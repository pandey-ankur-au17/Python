#using DP

class Solution:
    def climbStairs(n: int):
        steps = [1,1]
        for i in range(2,n+1):
            steps.append(steps[i-1] + steps[i-2])
        return steps[n]
    n=int(input("Enter the stairs:"))
    print(climbStairs(n))