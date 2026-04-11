class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(0, n+1):
            res = 0
            while i:
                i &= (i-1)
                res += 1
            l.append(res)
        return l
        