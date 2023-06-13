# https://leetcode.com/problems/valid-parentheses/
# Topic: Stack
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mappings:
                top = stack.pop() if stack else '#'
                if mappings[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
