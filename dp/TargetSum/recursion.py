# Time: 2^n 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        def backtrack(i, totalSoFar):
            if i == n:
                return 1 if totalSoFar == target else 0
            
            return (backtrack(i+1, totalSoFar+nums[i]) + backtrack(i+1, totalSoFar-nums[i]))
        
        return backtrack(0, 0)