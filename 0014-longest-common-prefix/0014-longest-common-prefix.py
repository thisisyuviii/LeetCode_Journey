class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        result =""
        base =strs[0]

        for i in range (len(base)):
            for j in strs [1:]:
                if i == len(j) or j[i] != base[i]:
                    return result
            result +=base[i]
        return result
        