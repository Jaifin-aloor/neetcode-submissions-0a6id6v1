class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        grid = [[float("inf") for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]

        for i in range(len(word2) + 1):
            grid[len(word1)][i] = len(word2) - i
        for j in range(len(word1) + 1):
            grid[j][len(word2)] = len(word1) - j

        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                if word1[i]==word2[j]:
                    grid[i][j] = grid[i+1][j+1]
                else:
                    grid[i][j] = 1 + min(grid[i+1][j], grid[i][j+1], grid[i+1][j+1])
        return grid[0][0]
        