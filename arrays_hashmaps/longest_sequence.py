class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        num_set = set(nums)
        longest_sequence = 0
        for x in num_set:
            current_number  = x
            if current_number-1 not in num_set:
                # this is the start of a sequence
                current_longest = 1
                while current_number+1 in num_set:
                    current_longest+=1
                    current_number+=1
                if current_longest>longest_sequence:
                    longest_sequence = current_longest
        return longest_sequence