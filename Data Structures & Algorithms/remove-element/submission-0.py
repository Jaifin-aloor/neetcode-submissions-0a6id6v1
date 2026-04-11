class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k, i = 0, 0
        while k < len(nums):
            if nums[k]==val: 
                k += 1
                continue
            nums[i] = nums[k]
            i += 1
            k += 1

        return i
        