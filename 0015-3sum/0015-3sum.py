class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Loop over all the nums and call that as the first element
        Perform 2 pointer search on the remaining array and see if the sum = 0
        """
        res = []
        nums.sort()
        for fid in range(len(nums)):
            f = nums[fid]
            if fid > 0 and nums[fid-1] == nums[fid]:
                continue 
            sid, tid = fid+1, len(nums)-1
            while sid < tid:
                if nums[sid] + nums[tid] + f == 0:
                    res.append([nums[sid], nums[tid], f]) 
                    sid += 1
                    tid -= 1
                    while sid < len(nums)  and nums[sid] == nums[sid-1]:
                        sid += 1
                elif nums[sid] + nums[tid] + f > 0:
                    tid -= 1
                else:
                    sid += 1
        return res