# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the
# resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# ● For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# ● For example, inverting [0,1,1] results in [1,0,0].
# Example 1:
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
from typing import List

class Solution:

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(image)):
            
            image[i].reverse()
            
            for j in range(len(image[i])):
                
                image[i][j]=int(not(image[i][j]))
        
        print(image)
                
        return image
        
    flipAndInvertImage(1,[[1,1,0],[1,0,1],[0,0,0]])

b=Solution()

