# https://leetcode.com/problems/majority-element/
# Topic: Array
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(n)
# HashMap
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        return max(counts.keys(), key=counts.get)

# Time Complexity: O(n)
# Space Complexity: O(1)
# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate