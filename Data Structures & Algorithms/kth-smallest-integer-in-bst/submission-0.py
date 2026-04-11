# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.nth, self.min = 0, float("-inf")
        self.k = k

        def dfs(node):
            if not node: return  
            dfs(node.left)
            self.nth += 1
            if self.nth == self.k:
                self.min = node.val  
                return    
            dfs(node.right)

        dfs(root)
        return self.min
    