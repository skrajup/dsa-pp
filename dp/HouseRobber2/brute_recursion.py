# time: 2^n
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i, ifr):
            if i >= len(nums):
                return 0
            if i == len(nums)-1 and ifr == True:
                return 0
            
            if i == 0:
                return max(nums[i]+dfs(i+2, True), dfs(i+1, False))
            else:
                return max(nums[i]+dfs(i+2, ifr), dfs(i+1, ifr))
            
        return dfs(0, False)
                