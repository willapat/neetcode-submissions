"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0

        start = []
        end = []
        for val in intervals:
            start.append(val.start)
            end.append(val.end)

        start.sort()
        end.sort()

        st, ed = 0, 0
        minRooms = 0
        while st < len(start):
            if start[st] < end[ed]:
                st += 1
                minRooms += 1
            else:
                ed += 1
                minRooms -= 1
            res = max(res, minRooms)
        return res