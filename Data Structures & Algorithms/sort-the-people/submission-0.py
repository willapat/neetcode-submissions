class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hp = []
        for i in range(0, len(names)):
            heapq.heappush(hp, (-heights[i], names[i]))
        res = []
        while hp:
            height, name = heapq.heappop(hp)
            res.append(name)

        return res