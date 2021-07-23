class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        
        start = 0
        end = len(matrix)
        
        if end == 0:
            return False
        
        while start < end:
            mid = (start + end) // 2
            
            s = 0
            e = len(matrix[mid])
        
            if e == 0:
                return False
            
            while s < e:
                m = (s+e)//2
                
                if matrix[mid][m] == target:
                    return True
                elif matrix[mid][m] < target:
                    s = m + 1
                else:
                    e = m
            
            if matrix[mid][0] > target:
                end = mid
            elif matrix[mid][-1] < target:
                start = mid + 1
            else:
                return False
        return False