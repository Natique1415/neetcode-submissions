class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isanagram(s1: str, s2: str) -> bool:
            if len(s1) != len(s2):
                return False
            return sorted(s1) == sorted(s2)

        res = []
        temp = []
        index_to_avoid = []
        
        for i in range(0,len(strs)):
             if (i not in index_to_avoid):
                temp.append(strs[i])

                for j in range(i + 1, len(strs)):
                    if isanagram(strs[i], strs[j]):
                        temp.append(strs[j])
                        index_to_avoid.append(j)

                res.append(temp)
                temp = []
    
        return res



        