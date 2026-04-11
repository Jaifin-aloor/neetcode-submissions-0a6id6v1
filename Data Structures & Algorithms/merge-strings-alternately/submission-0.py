class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res, i = "", 0
        l, r = 0, 0
        while l < len(word1) and r < len(word2):
            if i % 2 == 0 : 
                res += word1[l]
                l += 1
            else:
                res += word2[r]
                r += 1
            i += 1

        if word1[l:]: res += word1[l:]
        else: res += word2[r:]

        return res        