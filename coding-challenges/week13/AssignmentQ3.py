class Solution:
    def maxProfit(prices):
        max_profit = 0
        high_buy = 0
        
        prices = prices[::-1]
        
        for price in prices:
  
            if price > high_buy:
                high_buy = price
     
            if high_buy - price > max_profit:
                max_profit = high_buy - price

        return max_profit
    n=list(map(int, input().split()))
    print(maxProfit(n))