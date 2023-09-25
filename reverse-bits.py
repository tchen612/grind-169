# https://leetcode.com/problems/reverse-bits/
# Topic: Binary
# Difficulty: Easy

# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans