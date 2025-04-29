
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(coin_ind, total):
            print(f"call dfs({coin_ind}, {total})")
            if total == amount:
                print("1")
                return 1
            
            if total > amount or coin_ind >= len(coins):
                print("0") 
                return 0
            
            if (coin_ind, total) in dp:
                print(f"Value from dp: ({coin_ind}, {total})")
                return dp[(coin_ind, total)]
            
            # find total ways
            total_ways = 0
            for i in range(coin_ind, len(coins)):
                print(f"rec call dfs({i}, {total+coins[i]})")
                total_ways += dfs(i, total+coins[i])
            
            print(f"{total_ways}")
            dp[(coin_ind, total)] = total_ways
            return dp[(coin_ind, total)]
        
        return dfs(0, 0)


# Input: amount = 3, coins = [1,2]
# Call Steps:
# 
# ├── dfs(0,1)
# │   ├── dfs(0,2)
# │   │   ├── dfs(0,3) ✅ (Found 1 way)
# │   │   └── dfs(1,4) ❌
# │   └── dfs(1,3) ✅ (Found 1 way)
# └── dfs(1,2)
#     └── dfs(1,4) ❌
#
