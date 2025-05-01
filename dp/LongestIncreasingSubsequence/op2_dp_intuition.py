# time: n^2
# space: n
# come from last
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        lis = [0 for _ in range(len(nums))]
        lis[-1] = 1
        for i in range(len(nums)-2,-1,-1):
            j = i+1
            max_len = 1
            while j < len(nums):
                if nums[i] < nums[j]:
                    max_len = max(max_len, 1 + lis[j])
                j+=1
            lis[i] = max_len
    
        return max(lis)
