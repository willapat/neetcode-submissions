class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)
        for i in range(0, len(strs)):
            freq = sorted(Counter(strs[i]).items())
            dic[tuple(freq)].append(strs[i]) #need items or it only captures keys

        res = []
        for key in dic.keys():
            res.append(dic[key])
        
        return res
