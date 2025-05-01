# time: 2*N
class Solution:
    def distinctColoring (self, N, r, g, b):
        # code here 
        colors = [r,g,b]
        # pc = prev color
        dp = {}
        def dfs(i, pc):
            if i == N:
                return 0
            
            if (i,pc) in dp:
                return dp[(i,pc)]
            
            min_cost = float('inf')
            for color in range(3):
                if color != pc:
                    min_cost = min(min_cost, colors[color][i] + dfs(i+1,color))
            
            dp[(i,pc)] = min_cost
            return dp[(i,pc)]   
        
        return dfs(0, -1)
