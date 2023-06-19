# https://leetcode.com/problems/valid-palindrome/
# Topic: String
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = "".join(filter(str.isalnum, s.lower()))
        left = 0
        right = len(filtered_string) - 1
        while left < right:
            if filtered_string[left] != filtered_string[right]:
                return False
            left += 1
            right -= 1
        
        return True
