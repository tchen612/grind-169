# https://leetcode.com/problems/ransom-note/
# Topic: Hash Table
# Difficulty: Easy

# Time Complexity: O(m) where m is the length of the magazine
# Space Complexity: O(1)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
            
        letters = {}
        for letter in magazine:
            letters[letter] = letters.get(letter, 0) + 1

        for char in ransomNote:
            remaining = letters.get(char, 0) - 1
            if remaining < 0:
                return False
            letters[char] -= 1
        
        return True