# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Topic: Binary Search Tree
# Difficulty: Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time Complexity: O(n) (note for balance trees time complexity will be O(log(n)))
# Space Complexity: O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root

        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                return node