class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        res = []
        for i, val in hashmap.items():
            if val > len(nums)//3: res.append(i)
        return res
