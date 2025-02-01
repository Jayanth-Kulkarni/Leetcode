class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        timed = self.d
        timed[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        timed = self.d
        if key not in timed:
            return ""
        res = timed[key]
        result = ""
        l, r = 0, len(res) - 1
        while l <= r:
            mid = (l+r)//2
            if res[mid][1] == timestamp:
                return res[mid][0]
            if res[mid][1] > timestamp:
                r = mid - 1
            else:
                result = res[mid][0]
                l = mid + 1

        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)