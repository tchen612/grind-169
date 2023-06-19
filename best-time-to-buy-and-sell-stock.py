# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Topic: Array
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
