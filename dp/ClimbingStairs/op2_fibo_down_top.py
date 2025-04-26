# down top approach
class Solution:
    def climbStairs(self, n: int) -> int:
        # right = ways to reach top when at top
        # left = ways to reach top when at 1 level below top
        # now when at n-2: left + right
        # basically fibonacci
        left, right = 1, 1

        for i in range(n-1):
            temp = left
            left = left + right
            right = temp
        
        return left
