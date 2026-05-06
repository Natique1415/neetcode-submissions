class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
                                    
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        num = ""

        while i < len(s):

            while s[i] != "#":
                num += s[i]
                i += 1

            length = int(num)
            res.append(s[i + 1 : i + 1 + length])

            i = i + 1 + length
            num = ""

        return res
                        