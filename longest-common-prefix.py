# https://leetcode.com/problems/longest-common-prefix/
# Topic: String
# Difficulty: Easy

# Time Complexity: O(mn)
# Space Complexity: O(1)
# Vertical Scanning using zip()
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break
        
        return prefix

# Time Complexity: O(mn)
# Space Complexity: O(1)
# Vertical Scanning without using zip()
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs == None or len(strs) == 0: 
            return ""
        
        for i in range(len(strs[0])): 
            c = strs[0][i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        
        return strs[0]