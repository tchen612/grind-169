# https://leetcode.com/problems/first-bad-version/
# Topic: Binary Search
# Difficulty: Easy

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

# Time Complexity: O(log(n))
# Space Complexity: O(1)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            # if you need to avoid integer overflow in another language use: left + (right - left) // 2
            middle = (left + right) // 2
            
            if isBadVersion(middle) == False:
                left = middle + 1
            else:
                right = middle - 1

        return left
