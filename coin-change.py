# https://leetcode.com/problems/coin-change/
# Topic: Dynamic Prograaming
# Difficulty: Medium

# Time Complexity: O(S * n), where S is the amount and n is the number of different coins
# Space Complexity: O(S)
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != (amount + 1) else -1 

