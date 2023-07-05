# https://leetcode.com/problems/climbing-stairs/
# Topic: Dynamic Programming
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(n)
# Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
            
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Fibonacci Number
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        first  = 1
        second = 2

        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        
        return second