class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = [0]
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j:
                    length = min(heights[i],heights[j])
                    width = abs(i - j)
                    if max(areas) < (length*width):
                        areas.pop()
                        areas.append(length*width)
            
        return max(areas)
 
        