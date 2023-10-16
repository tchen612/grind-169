# https://leetcode.com/problems/3sum/
# Topic: Array
# Difficulty: Medium

# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Two Pointers
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, result)
        return result

    def twoSumII(self, nums: list[int], i: int, result: list[list[int]]):
        low = i + 1
        high = len(nums) - 1
        while (low < high):
            sum = nums[i] + nums[low] + nums[high]
            if sum < 0:
                low += 1
            elif sum > 0:
                high -= 1
            else:
                result.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1

# Time Complexity: O(n^2)
# Space Complexity: O(n)
# No Sort
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res