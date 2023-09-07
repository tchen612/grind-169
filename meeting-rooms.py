# https://leetcode.com/problems/meeting-rooms/
# Topic: Array
# Difficulty: Easy

# Time Complexity: O(nlog(n))
# Space Complexity: O(1)
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True