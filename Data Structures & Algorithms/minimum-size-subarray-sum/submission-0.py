class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minsub = float("inf")
        l, r = 0, 0
        summ = 0
        while r < len(nums):
            summ += nums[r]
            r += 1
            if summ >= target:
                while summ >= target:
                    summ -= nums[l]
                    l += 1
                minsub = min(minsub, r - l + 1)
            
        return minsub if minsub != float("inf") else 0