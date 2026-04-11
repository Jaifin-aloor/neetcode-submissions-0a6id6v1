class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        arr = [0] * 26
        arrs1 = [0] * 26
        for i in s1:
            arrs1[ord(i) - ord('a')] += 1

        l, r = 0, 0
        while r < len(s2):
            arr[ord(s2[r]) - ord('a')] += 1
            if len(s1) < (r - l + 1):
                arr[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if arr == arrs1: return True
            r += 1
        return False


        