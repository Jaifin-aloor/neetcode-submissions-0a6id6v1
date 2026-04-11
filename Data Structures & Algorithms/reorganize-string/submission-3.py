class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        max_freq = max(freq)
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        res = []
        while len(res) < len(s):
            maxIndex = freq.index(max(freq))
            char = chr(maxIndex + ord('a'))
            res.append(char)
            freq[maxIndex] -= 1
            if freq[maxIndex] == 0:
                continue

            tmp = freq[maxIndex]
            freq[maxIndex] = float("-inf")
            nextMaxIndex = freq.index(max(freq))
            char = chr(nextMaxIndex + ord('a'))
            res.append(char)
            freq[maxIndex] = tmp
            freq[nextMaxIndex] -= 1
        
        return "".join(res)

