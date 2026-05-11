class Solution:
    def isValid(self, s: str):
        stack = []
        for bracket in s:
            if self.isOpeningBracket(bracket):
                stack.append(bracket)

            else:
                if stack == []:
                    return False 
                if self.sameBracketType(stack[-1], bracket):
                    stack.pop()
                else: 
                    return False 

        if stack == []:
            return True
        return False

    def isOpeningBracket(self, bracket: str) -> bool:
        return bracket in ("(", "{", "[")

    def sameBracketType(self, b1: str, b2: str) -> bool:
        if (b1 == ")" and b2 == "(") or (b1 == "(" and b2 == ")"):
            return True

        if (b1 == "}" and b2 == "{") or (b1 == "{" and b2 == "}"):
            return True

        if (b1 == "]" and b2 == "[") or (b1 == "[" and b2 == "]"):
            return True

        return False