class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)
        for i in range(0, len(strs)):
            freq = sorted(Counter(strs[i]).items()) #dict
            dic[tuple(freq)].append(strs[i])

        res = []
        for key in dic.keys():
            res.append(dic[key])

        return res