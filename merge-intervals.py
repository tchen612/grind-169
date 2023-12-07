# https://leetcode.com/problems/merge-intervals/
# Topic: Array
# Difficulty: Medium

# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])
        result = []
        for interval in intervals:
          if not result or result[-1][1] < interval[0]:
            result.append(interval)
          else:
            result[-1][1] = max(result[-1][1], interval[1])
          
        return result