# https://leetcode.com/problems/k-closest-points-to-origin/
# Topic: Heap
# Difficulty: Medium

import heapq

# Time Complexity: O(nlog(k))
# Space Complexity: O(k)
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for (x, y) in points:
            # take negative of Euclidean distance to use heapq as a Max Heap
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
                
        return [(x, y) for (dist, x, y) in heap]