class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1) + 1, len(text2) + 1
        grid = [[0 for c in range(cols)] for r in range(rows)]
        for r in range(1, rows):
            for c in range(1, cols):
                if text1[r-1] == text2[c-1]:
                    grid[r][c] = 1 + grid[r-1][c-1]
                else:
                    grid[r][c] = max(grid[r][c-1], grid[r-1][c])
        return grid[rows-1][cols-1]


                    
                    
        