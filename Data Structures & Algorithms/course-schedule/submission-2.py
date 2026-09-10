class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #[0, 1] ---> take 1 before 0, then we need to check if 1 has any prereqs and so on

        dic = {} #dictionary of class --> prereqs
        for i in range(numCourses):
            dic[i] = []

        for x, y in prerequisites:
            dic[x].append(y)

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if dic[node] == []:
                return True
            
            visited.add(node)

            for edge in dic.get(node):
                if not dfs(edge):
                    return False
            visited.remove(node)
            dic[node] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
