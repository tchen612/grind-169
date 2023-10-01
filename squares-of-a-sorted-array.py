# https://leetcode.com/problems/squares-of-a-sorted-array/
# Topic: Array
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:   
        left = 0
        right = pointer = len(nums) - 1
        result = [0] * len(nums)

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[pointer] = square * square
            pointer -= 1

        return result