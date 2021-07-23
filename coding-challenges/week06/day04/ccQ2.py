from typing import List

class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:


        s=''.join(map(str,digits))
        k=str(int(s)+1)
        k=k.zfill(len(s))
        ans=list(map(int,k))

        print(ans)

        return ans
        
    plusOne(1,[1,2,3])

a=Solution()
