
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Use string library to remove all the special characters
        Remove all the spaces and convert the string to lowercase
        Start a left and right pointer at beginning and end of the string
        Compare both and keep moving them until left < right
        if they are not the same return false
        return true in the end
        """
        for special in string.punctuation:
            s = s.replace(special, "")
        s = s.replace(" ", "")
        s = s.lower()
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -= 1
        return True