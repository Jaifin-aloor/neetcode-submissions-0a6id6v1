class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k = 0, 0
        while i < len(nums):
            nums[k] = nums[i]
            while i < len(nums) and nums[i] == nums[k]:
                i += 1
            k += 1
        return k


        