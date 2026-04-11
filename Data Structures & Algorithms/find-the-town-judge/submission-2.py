class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustmap, negtrustmap = defaultdict(list), defaultdict(list)
        for i, j in trust:
            trustmap[i].append(j)
            negtrustmap[j].append(i)
        for key in range(1, n+1):
            if len(trustmap[key])==0 and len(negtrustmap[j])==n-1: return key
        return -1