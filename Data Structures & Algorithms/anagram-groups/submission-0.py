class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a key,value map, where the key is the dict and the value
        res = {}
        arr = []
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res.setdefault(tuple(count), []).append(s)

        for value in res.values():
            arr.append(value)
        
        return arr