
# #fibo using DP tabulation

# def fib(self, n: int) -> int:
#         a=[0]*(n+1)
#         if n==0:
#             return a[n]
#         a[1]=1
#         for i in range(2,n+1):
#             a[i]=a[i-1]+a[i-2]
#         return a[n]
# print(fib(1,45))

def fibo(no, dp):
    if no == 0:
        return 0
    
    if no == 1:
        return 1

    if dp[no] is not None:
        return dp[no]
        

    ans = fibo(no - 1, dp) + fibo(no - 2, dp)
    dp[no] = ans
    return ans

if __name__ == "__main__":
    dp = [None] * 10005
    print(fibo(135, dp))
