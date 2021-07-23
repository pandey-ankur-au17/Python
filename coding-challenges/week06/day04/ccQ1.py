from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop()

        print(nums)

        return nums

    rotate(1,[1,2,3,4,5],3)

a=Solution()
