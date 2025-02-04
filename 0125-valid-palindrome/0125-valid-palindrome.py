class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        s = s.lower().replace(" ","")
        for punc in string.punctuation:
            s = s.replace(punc, "")
        return s == s[::-1]