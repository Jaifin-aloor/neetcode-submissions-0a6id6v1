class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        self.maxarea = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            area = 1

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row in range(rows) and col in range(cols) and grid[row][col]==1):
                        grid[row][col] = 0
                        q.append((row, col))
                        area += 1
            self.maxarea = max(self.maxarea, area)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bfs(r, c)

        return self.maxarea




        