class Solution:
    import string
    def isPalindrome(self, s: str) -> bool:
        for punct in string.punctuation:
            if punct in s:
                s = s.replace(punct,"")
        s = s.replace(" ","").lower()
        return s == s[::-1]