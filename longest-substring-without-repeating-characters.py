# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Topic: String
# Difficulty: Medium

# Time Complexity: O(n)
# Space Complexity: O(m) // where m is length of charset
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        hashtable = {}

        left = 0
        # try to extend the range [i, j]
        for right in range(n):
            if s[right] in hashtable:
                left = max(hashtable[s[right]], left)

            ans = max(ans, right - left + 1)
            hashtable[s[right]] = right + 1

        return ans