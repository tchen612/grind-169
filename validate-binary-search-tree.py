# https://leetcode.com/problems/validate-binary-search-tree/
# Topic: Binary Search Tree
# Difficulty: Medium

import math
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            if root.val <= lower or root.val >= upper:
                return False
            stack.append((root.left, lower, root.val))
            stack.append((root.right, root.val, upper))
            
        return True
