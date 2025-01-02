class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        for punct in string.punctuation:
            s = s.replace(punct,"")
        s = s.replace(" ","").lower()
        return s==s[::-1]