class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)
        @lru_cache(None)
        def solve (i,MT,F):
            if i == n or MT ==0:
                return 0
            if F:
                sell = prices[i] + solve(i+1,MT-1,0)
                NS = solve(i+1,MT,1)
                return max(sell,NS)
            else:
                Buy = -prices[i] +solve(i+1,MT,1)
                NB=solve(i+1,MT,0)
                return max(Buy,NB)
        return solve(0,2,0)
        