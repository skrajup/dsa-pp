# Time: n*sum(nums)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        dp = {}
        def backtrack(i, totalSoFar):
            if i == n:
                return 1 if totalSoFar == target else 0
            
            if (i, totalSoFar) in dp:
                return dp[(i, totalSoFar)]
            
            dp[(i, totalSoFar)] = (backtrack(i+1, totalSoFar+nums[i]) + backtrack(i+1, totalSoFar-nums[i]))
            return dp[(i, totalSoFar)]

        return backtrack(0, 0)
        