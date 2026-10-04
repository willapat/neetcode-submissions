class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        sub = Counter(s1)
        left, right = 0, len(s1)
        while right <= len(s2):
            window = Counter(s2[left:right])
            if window == sub:
                return True
            right += 1
            left += 1
        return False