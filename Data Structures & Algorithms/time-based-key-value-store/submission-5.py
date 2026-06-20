class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.dic[key]) - 1
        prev = -1
        while left <= right:
            mid = (left + right) // 2
            if timestamp == self.dic[key][mid][1]:
                return self.dic[key][mid][0]
            elif timestamp > self.dic[key][mid][1]:
                left = mid + 1
            else:
                right = mid - 1
            if self.dic[key][mid][1] <= timestamp:
                prev = mid
        if prev != -1:
            return self.dic[key][prev][0]
        return ""