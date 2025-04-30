# n = length of string s
# m = number of words in wordDict
# L = max length of a word in wordDict
# time: O(n × m × L)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i >= len(s):
                return True

            if i in dp:
                return dp[i]

            for word in wordDict:
                if i + len(word) <= len(s) and word == s[i:i+len(word)]:
                    dp[i] = dfs(i+len(word))
                    if(dp[i]):
                        return True

            dp[i] = False
            return dp[i]
        
        return dfs(0)
        