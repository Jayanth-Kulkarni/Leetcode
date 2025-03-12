class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        start = 0
        total_array = []
        
        if sum(gas) - sum(cost) < 0:
            return -1
        
        for idx, (i, j) in enumerate(zip(gas, cost)):
            total_array.append(i-j)
            total += i-j
            if total < 0:
                total = 0
                start = idx + 1
        
        return start