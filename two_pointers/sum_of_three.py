def find_sum_of_three(nums, target):
   nums = sorted(nums)
   for idx,i in enumerate(nums):
      low = idx+1
      high = len(nums) - 1
      new_target = target-i
      while low<high:
         if new_target-nums[high]==nums[low]:
            return True
         elif new_target-nums[high]>nums[low]:
            low+=1
         else:
            high-=1
   return False


