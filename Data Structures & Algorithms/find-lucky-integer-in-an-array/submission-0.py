class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = Counter(arr)

        maxNum = float('-inf')
        for key, value in dic.items():
            if key == value:
                maxNum = max(maxNum, key)
        return maxNum if maxNum >= 0 else -1
            