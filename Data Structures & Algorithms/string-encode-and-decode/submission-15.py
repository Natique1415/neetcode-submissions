class Solution:

    def encode(self, words: List[str]) -> str:
        encoded = ""
        for word in words:
            encoded = encoded + f"{len(word)}#{word}"

        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0 
        decoded_word = []
        start_point = 0 

        while i < len(s):
            if s[i] == "#":
                len_word = int(s[start_point:i])
                decoded_word.append(s[i + 1: i + 1 + len_word])
                start_point = i + 1 + len_word
                i = i + 1 + len_word
            else:
                i += 1  
        return decoded_word
