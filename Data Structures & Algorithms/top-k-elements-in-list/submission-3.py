class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        
        l = []
        for key, v in hm.items():
            l.append([key, v])
        
        l.sort(key = lambda x:x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(l[i][0])
        return res