class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            window.append(r)

            # Remove the leftmost element if it is out of the current window's range
            if window[0] <= r - k:
                window.popleft()

            # Once we have the first full window, start recording max values
            if r >= k - 1:
                res.append(nums[window[0]])


        return res