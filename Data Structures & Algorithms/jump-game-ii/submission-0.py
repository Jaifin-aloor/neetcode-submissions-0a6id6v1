class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums)-1:
            fur = 0
            for i in range(l, r+1):
                fur = max(fur, i + nums[i])
            l = r + 1
            r = fur
            res += 1
        return res
        
            

