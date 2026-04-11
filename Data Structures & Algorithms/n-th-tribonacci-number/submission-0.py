class Solution:
    def tribonacci(self, n: int) -> int:
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(1)
        if n <= 2: return dp[n]
        for i in range(3, n+1):
            num = dp[-1] + dp[-2] + dp[-3]
            dp.append(num)
        return dp[-1]
        