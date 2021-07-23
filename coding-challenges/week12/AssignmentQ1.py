import heapq
class Solution:
    def topKFrequent(self,nums,k):
        nums = Counter(nums)
        
        output = []
        
        for num, freq in nums.items():
            output.append((-freq, num))
            
        heapq.heapify(output)
        
        arr = []
        
        for i in range(k):
            arr.append(heapq.heappop(output)[1])
        
            
        return arr