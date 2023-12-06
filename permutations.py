# https://leetcode.com/problems/permutations/
# Topic: Recursion
# Difficulty: Medium

# Time Complexity: O(n*n!)
# Space Complexity: O(n)
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(current: list[int]):
            if len(current) == len(nums):
                result.append(list(current))
                return
        
            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()

        result = []
        backtrack([])

        return result