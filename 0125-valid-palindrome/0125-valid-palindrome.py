class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lstrip().replace(" ","")
        for i in string.punctuation:
            s = s.replace(i, "")
        s = s.lower()
        print(s)
        return s == s[::-1]