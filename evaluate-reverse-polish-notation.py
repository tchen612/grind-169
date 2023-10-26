# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Topic: Stack
# Difficulty: Medium

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
                continue
        
            number_2 = stack.pop()
            number_1 = stack.pop()
            
            result = 0
            if token == "+":
                result = number_1 + number_2
            elif token == "-":
                result = number_1 - number_2
            elif token == "*":
                result = number_1 * number_2
            else:
                result = int(number_1 / number_2)
                
            stack.append(result)

        return stack.pop()