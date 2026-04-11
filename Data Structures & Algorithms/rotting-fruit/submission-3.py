class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rq, fs = deque(), set()
        
        def addfruit(r, c):
            if (r<0 or c<0 or r==rows or c==cols or grid[r][c]!=1):
                return
            grid[r][c] = 2
            rq.append([r, c])
            fs.remove((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rq.append([r, c])
                elif grid[r][c] == 1:
                    fs.add((r, c)) 

        counter = -1
        while rq:
            counter += 1
            for i in range(len(rq)):
                row, col = rq.popleft()
                addfruit(row + 1, col)
                addfruit(row - 1, col)
                addfruit(row, col + 1)
                addfruit(row, col - 1)

        if fs: return -1
        else: return counter if counter!=-1 else 0
            

        
        
        