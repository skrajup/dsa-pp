# time: 3*N
# space: O(1)
class Solution:
    def distinctColoring (self, N, r, g, b):
        dp = [r[0],g[0],b[0]]
        
        for i in range(1,N):
            curr = [0,0,0]
            curr[0] = r[i]+min(dp[1], dp[2])
            curr[1] = g[i]+min(dp[0], dp[2])
            curr[2] = b[i]+min(dp[0], dp[1])
            dp = curr
        
        return min(dp)
