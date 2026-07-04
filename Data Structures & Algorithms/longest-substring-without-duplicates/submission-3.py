class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        i = 0
        max_len = 0

        while i < len(s):
            if s[i] not in substring:
                substring += s[i]
                
                # if the element is the last as of now 
                if i == len(s) - 1:
                    max_len = max(max_len, len(substring))
            else:
                max_len = max(max_len, len(substring))
                substring = substring[substring.index(s[i]) + 1 :]
                substring += s[i]
                ...

            # max_len = max(max_len, len(substring))
            i += 1

        return max_len
