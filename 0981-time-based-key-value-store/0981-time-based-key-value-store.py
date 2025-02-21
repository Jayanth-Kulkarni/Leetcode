class TimeMap:

    def __init__(self):
        self.l = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.l[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        nums = self.l[key]
        l, r = 0, len(nums)-1
        res = ""
        while l <= r:
            m = (l+r)//2
            mid = nums[m]
            if mid[1] == timestamp:
                return mid[0]
            elif mid[1] > timestamp:
                r = m - 1
            elif mid[1] < timestamp:
                res = mid[0]
                l = m + 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)