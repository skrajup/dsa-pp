# time: 2^n
class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == '0': # can't decode string starting with '0'
                return 0
            
            ways = dfs(i+1) # decode single digit

            if i+1 < len(s) and 10 <= int(s[i:i+2]) <=26:
                ways += dfs(i+2)
            
            return ways
        return dfs(0)
