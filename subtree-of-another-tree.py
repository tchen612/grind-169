# https://leetcode.com/problems/subtree-of-another-tree/
# Topic: Binary Tree
# Difficulty: Easy

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity: O(
# Space Complexity: O(
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        https://leetcode.com/problems/subtree-of-another-tree/editorial/