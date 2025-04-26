# time: n, space = n
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(k):
            if k <= 2:
                return k
            if k in cache:
                return cache[k]
            
            cache[k] = dfs(k-1)+dfs(k-2)
            return cache[k]
        
        return dfs(n)
        