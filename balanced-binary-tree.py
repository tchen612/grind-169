# https://leetcode.com/problems/balanced-binary-tree/
# Topic: Binary Tree
# Difficulty: Easy

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]

    def helper(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if not root:
            return True, -1
        
        leftBalanced, leftHeight = self.helper(root.left)
        if not leftBalanced:
            return False, 0
        
        rightBalanced, rightHeight = self.helper(root.right)
        if not rightBalanced:
            return False, 0

        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
