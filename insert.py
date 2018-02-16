"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """

    def insert(self, intervals, newInterval):
        res = []
        tmp = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                res.append(interval)
                tmp += 1
            elif interval.start > newInterval.end:
                res.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        res.insert(tmp, newInterval)
        return res
