# n = length of string s

# m = number of words in wordDict
# time: m^n
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(i):
            if i >= len(s):
                return True

            for word in wordDict:
                if i + len(word) <= len(s) and word == s[i:i+len(word)]:
                    if(dfs(i+len(word))):
                        return True

            return False
        
        return dfs(0)
        