class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #max freq can be len of array
        dic = {i: [] for i in range(1, len(nums) + 1)}
        
        freq = Counter(nums)
        
        for key, value in freq.items():
            dic[value].append(key)
        
        res = []
        for i in range(len(nums), 0, -1):
            for val in dic[i]:
                if len(res) < k:
                    res.append(val)

        return res