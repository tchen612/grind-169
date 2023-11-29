# https://leetcode.com/problems/product-of-array-except-self/
# Topic: Array
# Difficulty: Medium

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [0] * n
        answer[0] = 1

        for i in range(1, n):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        right = 1
        for i in reversed(range(n)):
            answer[i] = answer[i] * right
            right *= nums[i]
        
        return answer

