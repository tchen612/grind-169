# https://leetcode.com/problems/diameter-of-binary-tree/
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
# Space Complexity: O(n), if the tree is balanced it will be log(n)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            nonlocal diameter
            left = longest_path(node.left)
            right = longest_path(node.right)

            diameter = max(diameter, left + right)

            return max(left, right) + 1
        
        longest_path(root)
        return diameter