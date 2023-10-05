# https://leetcode.com/problems/01-matrix/
# Topic: Graph
# Difficulty: Medium

from collections import deque

# Time Complexity: O(mn)
# Space Complexity: O(mn)
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:   
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        m = len(mat)
        n = len(mat[0])

        queue = deque([])
        seen = set()
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    seen.add((row, col))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            row, col = queue.popleft()
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
            
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    mat[next_row][next_col] = mat[row][col] + 1
                    queue.append((next_row, next_col))
                    seen.add((next_row, next_col))

        return mat