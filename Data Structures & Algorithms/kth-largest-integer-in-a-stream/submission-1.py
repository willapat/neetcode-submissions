class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for val in nums:
            heapq.heappush(self.heap, val)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) < self.k:
            return self.heap[0]
        
        removed = []
        for i in range(len(self.heap) - self.k):
            removed.append(heapq.heappop(self.heap))

        kth = self.heap[0]

        for val in removed:
            heapq.heappush(self.heap, val)

        return kth