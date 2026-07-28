# Time Complexity : O(m × k)
#k = number of digits in n (about log₁₀(n)).
#m = number of unique values encountered before reaching 1 or entering a cycle
class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()  # O(n)

        while n not in visit:
            visit.add(n)
            n=self.sumOfSquare(n)  # O(k)

            if n == 1:
                return True
        return False
    def sumOfSquare(self,n:int)->int:
        output=0

        while n :
            digit=n%10
            digit=digit ** 2
            output += digit
            n = n // 10
        return output
         
        