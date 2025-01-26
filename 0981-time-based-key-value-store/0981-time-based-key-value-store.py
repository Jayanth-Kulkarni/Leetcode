class TimeMap:

    def __init__(self):
        self.res = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.res[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        nums = self.res[key]
        l, r = 0, len(nums)-1
        res = ""
        while l <= r:
            mid = (l + r)//2
            if nums[mid][1] == timestamp:
                return nums[mid][0]
            elif nums[mid][1] > timestamp:
                r = mid-1
            else:
                res = nums[mid][0]
                l = mid+1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)