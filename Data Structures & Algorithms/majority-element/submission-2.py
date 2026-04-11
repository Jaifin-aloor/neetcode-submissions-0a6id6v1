class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
            if counter[i] > len(nums)//2:
                return i
        
        