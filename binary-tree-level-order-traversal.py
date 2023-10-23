# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Topic: Binary Tree
# Difficulty: Medium

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity: O(n)
# Space Complexity: O(n)
# Iteration
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root])
        while queue:
            levels.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1

        return levels

# Time Complexity: O(n)
# Space Complexity: O(n)
# Recursion
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        levels = []
        if not root:
            return levels

        def helper(node: Optional[TreeNode], level: int):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)

            if node.right:
                helper(node.right, level + 1)
        
        helper(root, 0)
        return levels