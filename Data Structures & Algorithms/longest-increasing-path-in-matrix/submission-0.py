class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {} # (r, c): lip
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, prev):
            if r<0 or c<0 or r==rows or c ==cols or matrix[r][c]<=prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = 1
            for dr, dc in directions:
                res = max(res, 1 + dfs(r+dr, c+dc, matrix[r][c]))
            dp[(r, c)] = res
            return res
        
        for r in range(rows): 
            for c in range(cols):
                dfs(r, c, -1)
        
        return max(dp.values())


        