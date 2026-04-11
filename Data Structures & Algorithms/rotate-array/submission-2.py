class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nums1 = [0] * l
        for i in range(l):
            nums1[(i+k) % l] = nums[i]

        nums[:] = nums1