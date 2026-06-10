class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1)
        freq_s1 = [0] * 26
        for i in range(len(s1)):
            index = ord(s1[i]) - ord("a")
            freq_s1[index] += 1
        while right <= len(s2):
            sub = s2[left:right]
            freq_sub = [0] * 26
            for i in range(len(sub)):
                index = ord(sub[i]) - ord("a")
                freq_sub[index] += 1
            if freq_sub == freq_s1:
                return True
            right += 1
            left += 1
        return False
