class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        print(count)
        res = [c for c,k in count[:k]]
        return res