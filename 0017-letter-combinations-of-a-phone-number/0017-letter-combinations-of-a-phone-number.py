class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dc = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def recurse(i, cur):
            if i == len(digits):
                res.append(cur[:])
                return res

            for c in dc[digits[i]]:
                recurse(i+1, cur+c)
        
        if digits == "":
            return []
        
        recurse(0, "")
        return res