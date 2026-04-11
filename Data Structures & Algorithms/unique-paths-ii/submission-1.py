class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        def helper(r, c):
            if r-1>=0 and c-1>=0: return (obstacleGrid[r][c-1] + obstacleGrid[r-1][c])
            if r-1>=0: return obstacleGrid[r-1][c]
            if c-1>=0: return obstacleGrid[r][c-1]
            return 1

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                    continue
                obstacleGrid[r][c] = helper(r, c)
                
        return obstacleGrid[rows-1][cols-1]
        