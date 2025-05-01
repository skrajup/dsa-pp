# time: 2^n ???
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # i = index
        # pn = prev number
        def dfs(i,pn):
            if i == len(nums):
                return 0
            
            if nums[i] > pn:
                return max(1+dfs(i+1,nums[i]), dfs(i+1, pn))
            
            return dfs(i+1,pn)

        return dfs(0,float('-inf'))
