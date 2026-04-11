class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[None] * (n+1) for _ in range(n)]
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n -2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i+1]

        def dfs(i, m):
            if i == n:
                return 0
            if dp[i][m] is not None:
                return dp[i][m]
            res = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                res = max(res, suffix_sum[i] - dfs(i + x, max(m, x)))
            dp[i][m] = res
            return res
        return dfs(0, 1)