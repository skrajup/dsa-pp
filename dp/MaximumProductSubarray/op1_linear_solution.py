# time: O(n)
# compute currMax and currMin on each num from left
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = nums[0],nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            currMax, currMin = max(nums[i]*currMax, nums[i]*currMin, nums[i]), min(nums[i]*currMax, nums[i]*currMin, nums[i])
            ans = max(ans, currMax)
        
        return ans
