#T(C):  O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pCount={}
        pSum=0
        pCount[0]=1
        count=0
        for i in range(n):
            pSum +=nums[i]

            remove = pSum - k
            if remove in pCount:
                count +=pCount[remove]

            pCount[pSum]=pCount.get(pSum,0)+1
        return count
             
