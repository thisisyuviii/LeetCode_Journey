#Time Complexity O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        num_set = set(nums)
        max_len = 1
        count = 1
    
        for num in num_set:
            start = num
            if start - 1 in num_set:
                continue
            while start + 1 in num_set:
                count += 1
                max_len = max(max_len, count)
                start = start + 1
            else:
                count = 1
    
        return max_len