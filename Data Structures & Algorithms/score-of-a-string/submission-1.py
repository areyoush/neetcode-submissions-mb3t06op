class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_values = []
        list2 = []
        for i in s:
            ascii_values.append(ord(i))

        for j in range(1, len(ascii_values)):
            list2.append(abs(ascii_values[j] - ascii_values[j-1]))

        return(sum(list2))
        