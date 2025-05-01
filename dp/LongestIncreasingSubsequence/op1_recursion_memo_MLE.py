# time: (n^2) ???
# space: n^2
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # i = index
        # pn = prev number
        dp = {}
        def dfs(i,pn):
            if i == len(nums):
                return 0
            
            if (i,pn) in dp:
                return dp[(i,pn)]

            if nums[i] > pn:
                dp[(i,pn)] = max(1+dfs(i+1,nums[i]), dfs(i+1, pn))
                return dp[(i,pn)]
            
            dp[(i,pn)] = dfs(i+1,pn)
            return dp[(i,pn)]

        return dfs(0,float('-inf'))