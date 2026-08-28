class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #how can we arrange the tasks to use min cpu cycles
        #if we heapify the tasks list
        mp = {}
        for task in tasks:
            if mp.get(task):
                mp[task] += 1
            else:
                mp[task] = 1
        
        heap = [-mp[key] for key in mp.keys()]
        heapq.heapify(heap)

        q = deque()
        time = 0
        while heap or q:
            if heap:
                value = heapq.heappop(heap)
                value += 1
                time += 1
                if value != 0:
                    q.append((value, time + n))
                if q and q[0][1] == time:
                    heapq.heappush(heap, q[0][0])
                    q.popleft() 
            else:
                time += 1
                if q and q[0][1] == time:
                    heapq.heappush(heap, q[0][0])
                    q.popleft()
        return time


            
