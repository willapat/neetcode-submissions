class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        frequency = [[] for _ in range(len(nums) + 1)]

        count = Counter(nums)
        for key, value in count.items():
            frequency[value].append(key)
        index = len(frequency) - 1
        while len(res) < k:
            current = frequency[index]
            for val in current:
                res.append(val)
                if len(res) >= k:
                    break
            index -= 1
        return res

