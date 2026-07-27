class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        for i in range(len(stones)):
            heap[i] = -stones[i]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if x > y:
                heapq.heappush(heap, -1 * (x - y))
            elif y > x:
                heapq.heappush(heap, -1 * (y - x))
        
        if heap:
            return -heap[0]
        else:
            return 0