
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(coin_ind, total):
            if total == amount:
                return 1
            
            if total > amount or coin_ind >= len(coins):
                return 0
            
            # find total ways
            pick = dfs(coin_ind, total+coins[coin_ind])
            skip = dfs(coin_ind+1, total)
            
            return pick+skip
        
        return dfs(0, 0)


