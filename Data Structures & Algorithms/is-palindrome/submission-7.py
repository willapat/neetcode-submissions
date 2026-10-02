class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        string = s.lower()
        while left < right:
            while left < right and not string[left].isalnum():
                left += 1
            while right > left and not string[right].isalnum():
                right -= 1
            
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True