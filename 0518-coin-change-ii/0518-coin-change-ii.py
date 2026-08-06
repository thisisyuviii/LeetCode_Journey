#Using Memo
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        memo=[[-1]*(amount+1) for _ in range(n+1)]

        def Solve(i,ts):
            if ts == 0:
                return 1
            if i == n:
                return 0
            if memo[i][ts] !=-1:
                return memo[i][ts]
            take = 0
            if coins[i]<=ts:
                take = Solve(i,ts-coins[i])
            
            Not_Take=Solve(i+1,ts)
            memo[i][ts]=take+Not_Take
            return memo[i][ts]
        return Solve(0,amount)
        