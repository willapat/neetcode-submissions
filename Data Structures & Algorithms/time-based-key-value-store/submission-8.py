class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if self.dic.get(key) == None:
            return res
        length = len(self.dic[key])
        left,right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            if self.dic[key][mid][0] == timestamp:
                res = self.dic[key][mid][1]
                return res
            elif self.dic[key][mid][0] > timestamp:
                right = mid - 1
            else:
                res = self.dic[key][mid][1]
                left = mid + 1
        
        return res
        
