class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        for k, v in counter.items():
            if v >= len(nums)//2:
                return k
        