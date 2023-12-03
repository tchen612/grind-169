# https://leetcode.com/problems/rotting-oranges/
# Topic: Graph
# Difficulty: Medium

from collections import deque

# Time Complexity: O(nm)
# Space Complexity: O(nm)
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque([])

        fresh_oranges = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        queue.append((-1, -1))
        minutes = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                minutes += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for direction in directions:
                    nrow, ncol = row + direction[0], col + direction[1]
                    if 0 <= nrow < num_rows and 0 <= ncol < num_cols and grid[nrow][ncol] == 1:
                        grid[nrow][ncol] = 2
                        fresh_oranges -= 1
                        queue.append((nrow, ncol))

        return minutes if fresh_oranges == 0 else -1