# time: 3*N
class Solution:
    def distinctColoring (self, N, r, g, b):
        # code here 
        colors = [r,g,b]
        # pc = prev color
        dp = [[0 for _ in range(len(colors))] for _ in range(N)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:
                    dp[i][j] = colors[j][i]
                else:
                    if j == 0:
                        dp[i][j] = colors[j][i]+min(dp[i-1][1], dp[i-1][2])
                    elif j == 1:
                        dp[i][j] = colors[j][i]+min(dp[i-1][0], dp[i-1][2])
                    else:
                        dp[i][j] = colors[j][i]+min(dp[i-1][0], dp[i-1][1])
        
        return min(dp[N-1])
