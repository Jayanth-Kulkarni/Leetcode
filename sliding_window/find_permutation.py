class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        question = {}
        for letter in s1:
            if letter in question:
                question[letter] +=1
            else:
                question[letter] = 1
        answer = {}
        for letter in s2[0:len(s1)]:
            if letter in answer:
                answer[letter] +=1
            else:
                answer[letter] = 1
        for i in range(0,len(s2)):
            if i==0:
                if answer == question:
                    return True
                continue
            start = i
            end = i+len(s1) 
            if (i+len(s1)) <= len(s2):
                answer[s2[start-1]] -= 1
                if answer[s2[start-1]] ==0:
                    del answer[s2[start-1]]
                if s2[end-1] in answer:
                    answer[s2[end-1]] +=1
                else:
                    answer[s2[end-1]] = 1
            if answer == question:
                return True
        return False

s = Solution()
s.checkInclusion("a","ab")