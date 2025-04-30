# time: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in dp:
                return dp[i]
            # rob it or not rob it
            dp[i] = max(nums[i] + dfs(i+2), dfs(i+1))

            return dp[i]

        return dfs(0)

