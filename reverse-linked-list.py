# https://leetcode.com/problems/reverse-linked-list/
# Topic: Linked List
# Difficulty: Easy

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity: O(
# Space Complexity: O(
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            next_temp = current.next
            current.next = previous
            previous = current
            current = next_temp
        
        return previous