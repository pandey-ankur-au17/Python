class Solution:
    def uniqueLetterString(self, s: str) -> int:
        prev = ans = 0
        d = {}
        for i,c in enumerate(s):
            k, j = d.get(c,[-1,-1])
            prev = prev + (i - j) - (j - k)
            d[c] = [j,i]
            ans += prev
        return ans
    s=input("String:")
    print(uniqueLetterString(1,s))