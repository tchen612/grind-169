# https://leetcode.com/problems/missing-number/
# Topic: Binary
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)
# Bit Manipulation
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = 0

        for i, num in enumerate(nums):
            result ^= i + 1
            result ^= num
        
        return result

# Time Complexity: O(n)
# Space Complexity: O(1)
# Gauss' Formula
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        expected = len(nums) * (len(nums) + 1) // 2
        actual = sum(nums)
        
        return expected - actual
        