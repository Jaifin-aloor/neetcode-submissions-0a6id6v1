class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[[0] * (n+1) for i in range(n+1)] for _ in range(2)]

        for i in range(n -1, -1, -1):
            for m in range(1, n + 1):
                total = 0
                dp[1][i][m] = 0
                dp[0][i][m] = float("inf")

                for x in range(1, 2 * m + 1):
                    if i + x > n:
                        break
                    total += piles[i + x - 1]
                    dp[1][i][m] = max(dp[1][i][m], total + dp[0][i+x][max(m,x)])
                    dp[0][i][m] = min(dp[0][i][m], dp[1][i+x][max(m,x)])
        return dp[1][0][1]