# https://leetcode.com/problems/contains-duplicate/
# Topic: Array
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
