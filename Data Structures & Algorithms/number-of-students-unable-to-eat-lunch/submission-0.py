class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        
        cycle = 0
        index = 0
        while queue:
            if queue[0] == sandwiches[index]:
                queue.popleft()
                index += 1
                cycle = 0
            else:
                rem = queue.popleft()
                queue.append(rem)
                cycle += 1
            if cycle >= len(queue):
                return len(queue)
        
        return 0