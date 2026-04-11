# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(node):
            if not node: return 0
            leftmax, rightmax = dfs(node.left), dfs(node.right)
            leftmax, rightmax = max(leftmax, 0), max(rightmax, 0)

            self.res = max(self.res, node.val + leftmax + rightmax)
            return node.val + max(leftmax, rightmax)
        
        dfs(root)
        return self.res
        