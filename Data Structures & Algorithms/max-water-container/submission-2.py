class Solution:
    def maxArea(self, height: List[int]) -> int:
            l = len(height)
            lp = 0
            rp = l - 1
            max_area = 0

            while lp < rp:
                length = min(height[lp],height[rp])
                width = (rp - lp)
                if max_area < (length*width):
                    max_area = length*width

                if height[lp] < height[rp]:
                    lp += 1 

                elif height[lp] > height[rp]:
                    rp -= 1 

                # height[lp] == height[rp]
                else:
                    lp += 1 
                    rp -= 1 
            
            return max_area
            
