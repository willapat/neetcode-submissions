class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        one, two = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            one[s[i]] = one.get(s[i], 0) + 1
            two[t[i]] = two.get(t[i], 0) + 1
        
        print(one)
        return one == two