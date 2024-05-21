class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        left,right = 0, n-1
        leftmost = 0
        rightmost = 0
        
        while left < right:
            if height[left] <= height[right]:
                if height[left] > leftmost:
                    leftmost = height[left]
                else:
                    res += leftmost - height[left]
                    left += 1
            if height[left] >= height[right]:
                if height[right] > rightmost:
                    rightmost = height[right]
                    
                else:
                    res += rightmost -height[right]
                    right -=1
        return res

