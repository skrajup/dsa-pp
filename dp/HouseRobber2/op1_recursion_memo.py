# time: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, ifr):
            if i >= len(nums):
                return 0
            if i == len(nums)-1 and ifr == True:
                return 0
            
            if (i, ifr) in dp:
                return dp[(i,ifr)]

            if i == 0:
                dp[(i,ifr)] = max(nums[i]+dfs(i+2, True), dfs(i+1, False))
            else:
                dp[(i,ifr)] = max(nums[i]+dfs(i+2, ifr), dfs(i+1, ifr))
            
            return dp[(i,ifr)]
            
        return dfs(0, False)
                