"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        curr = 0
        intervals.sort(key=lambda i: i.start)
        
        for interval in intervals:
            
            if curr <= interval.start:
                curr = interval.end
            else:
                return False 
        
        return True
