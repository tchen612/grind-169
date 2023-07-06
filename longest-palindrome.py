# https://leetcode.com/problems/longest-palindrome/
# Topic: String
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1), length of alphabet is fixed
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = set()
        for c in s:
            if c not in odds:
                odds.add(c)
            else:
                odds.remove(c)
        count = len(s) - len(odds) + bool(odds)
        return count