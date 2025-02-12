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
            num = nums[m][1]
            if num == timestamp:
                return nums[m][0]
            elif num > timestamp:
                r = m - 1
            else:
                res = nums[m][0]
                l = m + 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)