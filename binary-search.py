# https://leetcode.com/problems/binary-search/
# Topic: Binary Search
# Difficulty: Easy

# Time Complexity: O(log(n))
# Space Complexity: O(1)
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1
