# https://leetcode.com/problems/number-of-1-bits/
# Topic: Binary
# Difficulty: Easy

# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n-1)
            ans += 1
        return ans