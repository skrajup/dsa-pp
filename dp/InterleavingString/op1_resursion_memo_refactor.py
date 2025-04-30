# time: (m*n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        # k = i+j always
        def dfs(i,j):
            k = i+j
            if k == len(s3):
                return True
            
            if i == len(s1):
                return True if s2[j:] == s3[k:] else False

            if j == len(s2):
                return True if s1[i:] == s3[k:] else False
            
            if (i,j) in dp:
                return dp[(i,j)]

            if s1[i] == s2[j] == s3[k]:
                dp[(i,j)] = dfs(i+1,j) or dfs(i,j+1)
            elif s1[i] == s3[k]:
                dp[(i,j)] = dfs(i+1,j)
            elif s2[j] == s3[k]:
                dp[(i,j)] = dfs(i,j+1)
            else:
                dp[(i,j)] = False
            
            return dp[(i,j)]

        return dfs(0,0)                 
        