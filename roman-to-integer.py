# https://leetcode.com/problems/roman-to-integer/
# Topic: Math
# Difficulty: Easy

# Time Complexity: O(1), because of finite roman numerals
# Space Complexity: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = roman_numerals[s[-1]]
        for i in reversed(range(len(s)-1)):
            if roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                total -= roman_numerals[s[i]]
            else:
                total += roman_numerals[s[i]]
        return total