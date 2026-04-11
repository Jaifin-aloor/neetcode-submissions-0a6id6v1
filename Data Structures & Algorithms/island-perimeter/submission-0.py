class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def helper(r, c):
            res = 4
            for dr, dc in directions:
                if (r + dr)>=0 and (r +dr)!=rows and (c + dc)>=0 and (c + dc)!=cols and grid[r + dr][c + dc]==1:
                    res -= 1
            return res

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += helper(r, c)

        return perimeter