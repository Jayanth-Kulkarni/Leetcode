class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        state = defaultdict(int)
        l = r = max_length = max_freq = 0
        for r in range(len(s)):
            state[s[r]] += 1
            max_freq = max(max_freq, state[s[r]])

            if k + max_freq < r-l+1:
                state[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r-l+1)
        return max_length