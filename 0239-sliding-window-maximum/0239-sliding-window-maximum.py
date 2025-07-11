class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        window =deque()
        output = []
        for r in range(len(nums)):
            # Start emptying from the least element not the greatest!
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            window.append(r)

            if window[0] <= r-k:
                window.popleft()
            
            if r >= k-1:
                output.append(nums[window[0]])

        return output