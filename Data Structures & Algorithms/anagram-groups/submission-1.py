class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #i think I remember that we need the key to be the letters and val is the list
        dic = defaultdict(list)
        for n in strs:
            freq = [0] * 26
            for m in n:
                freq[ord(m) - ord("a")] += 1
            dic[tuple(freq)].append(n)

        return list(dic.values())