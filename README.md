# Grind 169

## List of questions
https://www.techinterviewhandbook.org/grind75?weeks=26&hours=7

## Template
```
# <url to LeetCode>
# Topic: <topic>
# Difficulty: <difficulty>

# Time Complexity: <time_complexity>
# Space Complexity: <space_complexity>
class Solution:
    <solution here>
```

### Example
```
# https://leetcode.com/problems/two-sum/
# Topic: Array
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [i, seen[diff]]
            seen[num] = i
```
