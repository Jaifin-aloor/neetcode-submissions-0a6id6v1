class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x in [1, 2, 3]: return 1
        l, r = 0, x//2
        while l <= r :
            mid = (l + r)//2
            if mid * mid == x: return mid
            elif mid * mid > x : r = mid - 1
            else : l = mid + 1
        return l - 1


        