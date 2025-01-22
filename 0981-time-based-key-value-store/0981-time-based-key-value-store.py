class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        store = self.d
        store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        store = self.d
        result = ""
        if key not in store:
            return result
        else:
            nums = store[key]
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l+r)//2
                if nums[mid][1] == timestamp:
                    return nums[mid][0]
                elif nums[mid][1] > timestamp:
                    r = mid - 1
                else:
                    l = mid + 1
                    result = nums[mid][0]
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)