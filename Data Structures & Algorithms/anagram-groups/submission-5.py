class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for char in string:
                arr[ord(char) - ord('a')] += 1
            dic[tuple(arr)].append(string)
        
        res = []
        for key in dic.keys():
            res.append(dic[key])
        return res