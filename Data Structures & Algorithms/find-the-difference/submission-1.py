class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        one = Counter(s)
        two = Counter(t)

        for key,value in two.items():
            if two[key] != one.get(key, 0):
                return key
        

        