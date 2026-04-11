# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            res.append(q[-1].val)
            for i in range(qlen):
                a = q.popleft()
                if a.left: q.append(a.left)
                if a.right: q.append(a.right)

        return res

        