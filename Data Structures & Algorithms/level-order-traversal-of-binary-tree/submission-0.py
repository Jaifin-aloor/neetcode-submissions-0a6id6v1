# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        q.append([root, 1])
        
        while q:
            a, level = q.popleft()
            if a:
                q.append([a.left, level + 1])
                q.append([a.right, level + 1])
            else: continue

            if len(res) == level:
                res[-1].append(a.val)
            else: res.append([a.val])


        return res
            


        