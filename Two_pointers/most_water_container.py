class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l = 0
        r= len(height)-1
        while(l<r):
            area = min(height[l],height[r])*(r-l)
            maxArea = max(maxArea, area)
            #problem is better iteration 
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
