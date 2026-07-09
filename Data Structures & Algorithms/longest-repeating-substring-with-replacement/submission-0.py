class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        count = {}


        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            lenOfWindow = r - l + 1 

            if (lenOfWindow - max(count.values()) <= k):
                res = max(res,lenOfWindow)
            
            else:
                while (r - l + 1) - max(count.values()) > k:
                    count[s[l]] -= 1 
                    l += 1 


        return res
        