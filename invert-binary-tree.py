# https://leetcode.com/problems/invert-binary-tree/
# Topic: Binary Tree
# Difficulty: Easy

from typing import Collection, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity: O(n)
# Space Complexity: O(n)
# Recursion (DFS)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            right = self.invertTree(root.right)
            left = self.invertTree(root.left)
            
            root.left = right
            root.right = left

        return root

# Time Complexity: O(n)
# Space Complexity: O(n)
# Iterative (BFS)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            queue = Collection.deque([root])
            while queue:
                current = queue.popleft()
                current.left, current.right = current.right, current.left
                
                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)
        
        return root