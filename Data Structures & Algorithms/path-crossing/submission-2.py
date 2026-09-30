class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W':(-1, 0)}
        curr = (0, 0)
        s.add(curr)
        for i in range(0, len(path)):
            new = directions[path[i]]
            curr = (curr[0] + new[0], curr[1] + new[1])
            if curr in s:
                return True
            s.add(curr)

        return False