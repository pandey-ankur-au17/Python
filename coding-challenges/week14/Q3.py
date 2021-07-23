class Solution:
    def maximumWealth(self, accounts) -> int:
        wealth  = -1
        for i in accounts:
            wealth  = max(wealth , sum(i))
        return wealth 