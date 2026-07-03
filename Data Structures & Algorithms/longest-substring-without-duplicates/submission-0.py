class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring, i = 0, 0
        substring = ""
        while i < len(s):
            if s[i] not in substring:
                substring += s[i]

            else:
                longestSubstring = max(longestSubstring,len(substring))
                substring = substring[substring.index(s[i]) + 1:]
                substring += s[i]

            # this is for the case if a string is perfect and does not go to else clause
            longestSubstring = max(longestSubstring,len(substring))
            i += 1 

        return longestSubstring