class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isanagram(s1: str, s2: str) -> bool:
            if len(s1) != len(s2):
                return False
            return sorted(s1) == sorted(s2)

        res = []
        temp = []
        
        for i in range(0,len(strs)):
             if any(strs[i] in sublist for sublist in res) == False:
                temp.append(strs[i])

                for j in range(i + 1, len(strs)):
                    if isanagram(strs[i], strs[j]):
                        temp.append(strs[j])

                res.append(temp)
                temp = []
    
        return res



        