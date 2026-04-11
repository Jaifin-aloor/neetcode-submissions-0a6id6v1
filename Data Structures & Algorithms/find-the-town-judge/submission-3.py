class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustmap, negtrustmap = defaultdict(int), defaultdict(int)
        for i, j in trust:
            trustmap[i] += 1
            negtrustmap[j] += 1
        for key in range(1, n+1):
            if trustmap[key]==0 and negtrustmap[j]==n-1: return key
        return -1