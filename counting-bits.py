# https://leetcode.com/problems/counting-bits/
# Topic: Binary
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans 