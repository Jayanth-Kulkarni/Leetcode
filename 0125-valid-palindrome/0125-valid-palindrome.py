class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^0-9a-zA-Z]", "", s)
        s = s.lower()
        l, r = 0, len(s) - 1
        print(s)
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True