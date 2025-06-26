class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Process 
        1. Have a prefix product calculated till the index
        2. Have a postfix product calculated till the index in reverse order
        3. If prefix[i-1] and postfix[i+1] exist, then result[i] = prefix[i-1] * postfix[i+1]
        4. Otherwise result[i] = ?
        """
        prefix, postfix = [nums[0]], [nums[-1]]
        for i in nums[1:]:
            prefix.append(prefix[-1] * i)
        reverse = nums[::-1]
        for i in reverse[1:]:
            postfix.append(postfix[-1] * i)
        postfix = postfix[::-1]
        result = []
        for i in range(len(nums)):
            if i-1 >= 0 and i+1 < len(nums):
                result.append(prefix[i-1] * postfix[i+1])
            elif i-1 >= 0:
                result.append(prefix[i-1])
            elif i+1 < len(nums):
                result.append(postfix[i+1])
        return result