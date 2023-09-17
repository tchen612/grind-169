# https://leetcode.com/problems/single-number/
# Topic: Binary
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor