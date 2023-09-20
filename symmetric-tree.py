# https://leetcode.com/problems/symmetric-tree/
# Topic: Binary Tree
# Difficulty: Easy

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
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root.left, root.right])
        while queue:
            node1, node2 = queue.popleft(), queue.popleft()
            if not node1 and not node2:
                continue
            elif (not node1 or not node2) or (node1.val != node2.val):
                return False

            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)

        return True
