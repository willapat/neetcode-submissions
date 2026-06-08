class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # []. []. []. []. []
        freq = [[] for _ in range(len(nums) + 1)]
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        for key, value in dic.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res