class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        res = ""
        while l < len(word1) and r < len(word2):
            res += word1[l]
            l += 1
            res += word2[r]
            r += 1
        
        if l < len(word1):
            res += word1[l:]
        else:
            res += word2[r:]
        
        return res