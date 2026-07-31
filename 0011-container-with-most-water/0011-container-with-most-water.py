class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height) -1
        base=0
        while left < right :
            currentMax= min(height[left],height[right])*(right-left)
            base=max(currentMax,base)
            if height[left] < height[right]:
                left+=1
            else:
                right -=1
        return base