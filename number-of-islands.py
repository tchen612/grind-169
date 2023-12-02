# https://leetcode.com/problems/number-of-islands/
# Topic: Graph
# Difficulty: Medium

from collections import deque

# Time Complexity: O(nm)
# Space Complexity: O(min(n,m))
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        directions = [(0,1), (0,-1), (-1,0), (1,0)]

        queue = deque([])
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    queue.append((i, j))
                    while queue:
                        r, c = queue.popleft()
                        for direction in directions:
                            nr, nc = r + direction[0] , c + direction[1]
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1':
                                queue.append((nr, nc))
                                grid[nr][nc] = '0'
                    num_islands += 1

        return num_islands