class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs: return ""
        res = len(strs[0])
        for i in range(1, len(strs)):
            for j in range(min(res, len(strs[i]))):
                if len(strs[i]) < res: res = len(strs[i])
                if strs[i][j] != strs[0][j]:
                    res = j
                    break
        
        return "" if not res else strs[0][:res]


        