# time: 38*n, space: n
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def dfs(i):
            n = len(days)
            if i >= n:
                return 0

            if i in dp:
                return dp[i]
            
            second_ind, seventh_ind, thirtieth_ind = n+1,n+1,n+1

            if i+1 < n:
                second_ind = i+1
            
            j = i
            day = days[i]
            while j < n and days[j] < day + 7:
                j+=1
            seventh_ind = j

            j = i
            while j < n and days[j] < day + 30:
                j+=1
            thirtieth_ind = j
            
            dp[i] = min(costs[0]+dfs(second_ind), costs[1]+dfs(seventh_ind), costs[2]+dfs(thirtieth_ind))
            return dp[i]
        return dfs(0)

# Call Steps: Caching reduced time: less calls
# Function Call: 0
# Function Call: 1
# Function Call: 2
# Function Call: 3
# Function Call: 4
# Function Call: 5
# Function Call: 6
# Function Call: 7
# Function Call: 8
# Function Call: 9
# Function Call: 10
# Function Call: 11
# Value retrieved from dp: 10
# Value retrieved from dp: 10
# Value retrieved from dp: 10
# Value retrieved from dp: 10
# Value retrieved from dp: 10
# Value retrieved from dp: 10
# Value retrieved from dp: 10
# Value retrieved from dp: 9
# Value retrieved from dp: 8
# Value retrieved from dp: 7
# Value retrieved from dp: 11