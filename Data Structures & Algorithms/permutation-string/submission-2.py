class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1)
        
        freq_s1 = [0] * 26
        freq_sub = [0] * 26
        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord("a")] += 1
            freq_sub[ord(s2[i]) - ord("a")] += 1

        if freq_sub == freq_s1:
                return True

        while right < len(s2):
            freq_sub[ord(s2[left]) - ord("a")] -= 1
            freq_sub[ord(s2[right]) - ord("a")] += 1
            
            if freq_sub == freq_s1:
                return True
            right += 1
            left += 1
        return False
