class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        maxa = 0
        alpha = [0] * 26
        for r in range(len(s)):
            alpha[ord(s[r]) - ord("A")] += 1
            maxa = max(maxa, alpha[ord(s[r]) - ord("A")])
            length = r - l + 1
            if length - maxa <= k:
                res = max(res, length)
            else:
                alpha[ord(s[l]) - ord("A")] -= 1
                l += 1
        return res

        
        