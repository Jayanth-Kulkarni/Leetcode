from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonic deque: holds indices of elements in decreasing order of their values
        window = deque()
        output = []

        for r in range(len(nums)):
            # Remove elements from the back that are smaller than the current element
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            window.append(r)

            # Remove the leftmost element if it is out of the current window's range
            if window[0] <= r - k:
                window.popleft()

            # Once we have the first full window, start recording max values
            if r >= k - 1:
                output.append(nums[window[0]])

        return output
