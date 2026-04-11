class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1) + 1, len(text2) + 1
        grid = [[0 for c in range(cols)] for r in range(rows)]
        for r in range(rows-2, -1, -1):
            for c in range(cols-2, -1, -1):
                if text1[r] == text2[c]:
                    grid[r][c] = 1 + grid[r+1][c+1]
                else:
                    grid[r][c] = max(grid[r][c+1], grid[r+1][c])
        return grid[0][0]


                    
                    
        