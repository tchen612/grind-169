# https://leetcode.com/problems/combination-sum/
# Topic: Array
# Difficulty: Medium

# Time Complexity: O(N^((T/M)+1)) where N is the number of candidates, T is the target value and M is the minimal value among the candidates
# Space Complexity: O(T/M)
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []

        def backtrack(remainder: int, combination: list[int], start: int):
            if remainder == 0:
                results.append(list(combination))
                return
            elif remainder < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(remainder - candidates[i], combination, i)
                combination.pop()

        backtrack(target, [], 0)
        return results
