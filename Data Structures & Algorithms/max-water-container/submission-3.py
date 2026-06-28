class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j:
                    length = min(heights[i],heights[j])
                    width = abs(i - j)
                    if max_area < (length*width):
                        max_area = length*width
            
        return max_area
 
        