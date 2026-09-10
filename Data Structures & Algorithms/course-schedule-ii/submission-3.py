class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #if there is a loop, we want to return an empty array
        #if we never find a loop, we can take all classes
        #return the order in which we take those classes

        dic = defaultdict(list)
        for a, b in prerequisites:
            dic[a].append(b)

        visited = set()
        completed = set()
        def dfs(course):
            if course in visited:
                return False
            if course in completed:
                return True

            visited.add(course)
            for edge in dic[course]:
                if not dfs(edge):
                    return False

            res.append(course)
            visited.remove(course)
            completed.add(course)
            return True


        res = []
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res