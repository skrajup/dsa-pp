# time: 2^n
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i):
            if i >= len(nums):
                return 0
            
            # rob it or not rob it
            return max(nums[i] + dfs(i+2), dfs(i+1))
        
        return dfs(0)
        