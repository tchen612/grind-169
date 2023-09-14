# https://leetcode.com/problems/middle-of-the-linked-list/
# Topic: Linked List
# Difficulty: Easy

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow