# coin_ind → can go from 0 to len(coins)

# total → can go from 0 to amount

# Time: O(len(coins) × amount)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(coin_ind, total):
            # print(f"call dfs({coin_ind}, {total})")
            if total == amount:
                # print("1")
                return 1
            
            if total > amount or coin_ind >= len(coins):
                # print("0") 
                return 0
            
            if (coin_ind, total) in dp:
                # print(f"Value from dp: ({coin_ind}, {total})")
                return dp[(coin_ind, total)]
            
            # find total ways
            pick = dfs(coin_ind, total+coins[coin_ind])
            skip = dfs(coin_ind+1, total)
            dp[(coin_ind, total)] = pick + skip
            
            # print(f"{dp[(coin_ind, total)]}")
            return dp[(coin_ind, total)]
        
        return dfs(0, 0)

