# time: 2^(m+n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if text1[i] == text2[j]:
                return 1+dfs(i+1,j+1)
            else:
                return max(dfs(i,j+1), dfs(i+1,j))
            
        return dfs(0,0)
