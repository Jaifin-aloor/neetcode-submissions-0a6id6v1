class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res1, res2 = 0, 0
        n = len(nums)
        for i in range(n+1):
            if i < n: res2 ^= nums[i]
            res1 ^= i
        return res1 ^ res2
