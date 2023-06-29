# https://leetcode.com/problems/flood-fill/
# Topic: Graph
# Difficulty: Easy

from collections import deque

# Time Complexity: O(nm)
# Space Complexity: O(nm)
# BFS
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        oldColor = image[sr][sc]
        m = len(image)
        n = len(image[0])

        if oldColor != color:
            queue = deque([(sr, sc)])
            while queue:
                i, j = queue.popleft()
                image[i][j] = color
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == oldColor: 
                        queue.append((x, y))
        
        return image

# Time Complexity: O(nm)
# Space Complexity: O(nm)
# DFS
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        oldColor = image[sr][sc]
        m = len(image)
        n = len(image[0])
        
        if oldColor == color:
            return image

        stack = [(sr, sc)]
        while stack:
            i, j = stack.pop()
            image[i][j] = color
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == oldColor: 
                    stack.append((x, y))
        
        return image