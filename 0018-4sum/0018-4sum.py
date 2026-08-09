class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        my_set=set()
        for i in range(n):
            for j in range(i+1,n):
                hashset=set()
                for k in range(j+1,n):
                    fourth=target-(nums[i]+nums[j]+nums[k])
                    if fourth in hashset:
                        temp=[nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        my_set.add(tuple(temp))
                    hashset.add(nums[k])           
        result=[]   
        for ans in my_set:
            result.append(list(ans))
        return result                
