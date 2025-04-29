class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def dfs(total):
            # print(f"call dfs({total})")
            if total == amount:
                # print("1")
                return 1
            
            if total > amount:
                # print("0") 
                return 0
            
            # find total ways
            total_ways = 0
            for den in coins:
                # print(f"rec call dfs({total+den})")
                total_ways += dfs(total+den)
            
            # print(f"{total_ways}")
            return total_ways
        
        return dfs(0)

# Issue with your code:

# You are trying every coin at every step, which is fine.
# But you allow picking coins in any order every time (all coins from index 0 again).
# This leads to overcounting many combinations multiple times.

# ➡ Order matters in your recursion now — but in the problem, order doesn't matter.
