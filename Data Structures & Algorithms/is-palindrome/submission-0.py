class Solution:
    def isPalindrome(self, s: str) -> bool:
        iss = ""
        
        for ss in s: 
            if (ss.isalnum()):
                iss += ss

        return iss.lower() == iss[::-1].lower()
        