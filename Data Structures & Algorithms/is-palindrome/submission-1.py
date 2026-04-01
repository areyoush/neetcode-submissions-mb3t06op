import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)
        input_string = ''.join(cleaned_string)
        inverted_string = input_string[::-1]
        

        
        return (inverted_string.lower() == input_string.lower())