class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dc = {"2" :"abc",
            "3" :"def",
            "4" :"ghi",
            "5" :"jkl",
            "6" :"mno",
            "7" :"pqrs",
            "8" :"tuv",
            "9" :"wxyz"}
        
        def recurse(i, cur):
            if i == len(digits):
                res.append(cur[:])
                return
            
            for d in dc[digits[i]]:
                recurse(i+1, cur+d)
        
        if digits == "":
            return []
        
        recurse(0, "")

        return res