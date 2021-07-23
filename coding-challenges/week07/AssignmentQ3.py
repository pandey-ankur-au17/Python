# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]




class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
     
        def binary_search(nums,l,r,target):
            if l>r:
                return [-1,-1]
            mid=l+(r-l)//2
            if nums[mid]==target:
                while mid>=0 and nums[mid]==target:
                    mid-=1
                mid+=1
                start=mid
                while mid<=r and nums[mid]==target:
                    mid+=1
                mid-=1
                end=mid
                return [start,end]
            
            elif nums[mid]>target:
                return binary_search(nums,l,mid-1,target)
            else:
                return binary_search(nums,mid+1,r,target)
    
        
        return binary_search(nums,0,len(nums)-1,target)