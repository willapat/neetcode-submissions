class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # make a max heap, when the size of the max heap is greater than k
        # remove the top element, this leaves k smaller elements

        res = []
        heap = []

        for point in points:
            x1 = point[0]
            y1 = point[1]

            dist = math.sqrt((x1)**2 + (y1)**2)
            data = (-dist, point)

            heapq.heappush(heap, data)
            
            if len(heap) > k:
                heapq.heappop(heap)

        
        while heap:
            data = heapq.heappop(heap)
            res.append(data[1])

        return res