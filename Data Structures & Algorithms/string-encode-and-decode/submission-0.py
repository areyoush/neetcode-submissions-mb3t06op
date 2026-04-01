from typing import List
class Solution:
    def __init__(self):
        self.myhashmap = {}

    def encode(self, strs: List[str]) -> tuple:
        
        
        for index, value in enumerate(strs):
            length = len(value)
            self.myhashmap[index] = length

        s = "".join(strs)
        return s

    def decode(self, s: str) -> List[str]:
        word_list = []
        start = 0
        for index in sorted(self.myhashmap.keys()):
            word_length = self.myhashmap[index]
            word = s[start:start + word_length]
            word_list.append(word)
            start += word_length
        return word_list


