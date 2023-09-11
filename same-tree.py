# https://leetcode.com/problems/same-tree/
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True

        queue = deque([(p, q)])
        while queue:
            left, right = queue.popleft()
            if not check(left, right):
                return False
            
            if left:
                queue.append((left.left, right.left))
                queue.append((left.right, right.right))

        return True