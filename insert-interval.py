# https://leetcode.com/problems/insert-interval/
# Topic: Array
# Difficulty: Medium

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        start = newInterval[0]
        end = newInterval[1]
        left = []
        right = []

        for interval in intervals:
            if interval[1] < start:
                left.append(interval)
            elif interval[0] > end:
                right.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])

        return left + [[start,end]] + right
