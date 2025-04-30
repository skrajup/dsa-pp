# time: 2^(m+n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        def dfs(i,j,k):
            if k == len(s3):
                return True
            
            if i == len(s1):
                return True if s2[j:] == s3[k:] else False

            if j == len(s2):
                return True if s1[i:] == s3[k:] else False

            if s1[i] == s2[j] == s3[k]:
                return dfs(i+1,j,k+1) or dfs(i,j+1,k+1)
            elif s1[i] == s3[k]:
                return dfs(i+1,j,k+1)
            elif s2[j] == s3[k]:
                return dfs(i,j+1,k+1)
            else:
                return False

        return dfs(0,0,0)                 
