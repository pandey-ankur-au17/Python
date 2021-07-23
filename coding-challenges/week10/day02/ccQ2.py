def sumOfUnique(nums):
    
    hashing = {}
    for i in nums:
        if i in hashing.keys():
            hashing[i] += 1
        else:
            hashing[i] = 1

    sum = 0
    for k, v in hashing.items():
        if v == 1: sum += k
    return sum
nums = [1,2,3,2]
ans = sumOfUnique(nums)
print(ans)
