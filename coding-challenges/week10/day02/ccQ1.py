def findDuplicate(nums):
    first = nums[0]
    second = nums[nums[0]]
   
    while first != second: 
        first = nums[first]
        second = nums[nums[second]]
    first = 0
    while first != second: 
        first = nums[first] 
        second = nums[second]
    return first

nums = [1,3,4,2,2]
ans = findDuplicate(nums)
print(ans)
