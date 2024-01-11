class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxSize = 0
        while left < right:
            maxSize = max(maxSize,min(height[right],height[left])*(right-left))
            if min(height[right],height[left]) == height[right]:
                right -=1
            else:
                left +=1
        return maxSize
        