class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findTilt(self, root: TreeNode) -> int:

        self.res = 0
        node = root
        def helper(node):

            if node==None:              
                return 0
            else:
                
                l = helper(node.left)
                r = helper(node.right)
                self.res+=abs(r-l)
                return r+l+node.val

        helper(node)
        return self.res