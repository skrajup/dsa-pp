# m*n
# m*n + m+n
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            if text1[i] == text2[j]:
                dp[(i,j)] = 1+dfs(i+1,j+1)
            else:
                dp[(i,j)] = max(dfs(i,j+1), dfs(i+1,j))
            return dp[(i,j)]
            
        return dfs(0,0)