class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify(heap) #creates min heap

        while len(heap) > 1:
            order = []
            while heap:
                order.append(heapq.heappop(heap))

            x = order[-2]
            y = order[-1]

            if x == y:
                order.remove(x)
                order.remove(y)
            elif x > y:
                order.remove(y)
                order[-2] = x - y
            else:
                order.remove(x)
                order[-1] = y - x

            heap = order
            heapq.heapify(heap)
        
        if heap:
            return heap[0]
        else:
            return 0