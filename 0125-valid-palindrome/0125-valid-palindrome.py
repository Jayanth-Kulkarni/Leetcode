class Solution:
    import string
    def isPalindrome(self, s: str) -> bool:
        for char in string.punctuation:
            s = s.replace(char,"")
        s = s.replace(" ","").lower()
        return s==s[::-1]