class Solution:
    def firstUniqChar(self, s: str) -> int:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        indexes = []
        for x in alpha:
            if s.count(x)==1:
                indexes.append(s.index(x))
        try:
            return min(indexes)
        except:
            return -1