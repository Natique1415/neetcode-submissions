class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        substring = ""

        for r in range(len(s)):
            if s[r] in substring:
                substring = substring[substring.index(s[r]) + 1:]
                substring += s[r]
            
            # s[r] not in substring
            else:
                substring += s[r]

            res = max(res,len(substring)) 
        return res
        