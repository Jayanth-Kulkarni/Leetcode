class TimeMap:

    def __init__(self):
        self.l = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.l[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        d = self.l[key]        
        l, r = 0, len(d)-1
        res = ""
        while l <= r:
            mid = (l+r)//2
            if d[mid][1] == timestamp:
                return d[mid][0]
            elif d[mid][1] > timestamp:
                r = mid - 1
            elif d[mid][1] < timestamp:
                res = d[mid][0]
                l = mid + 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)