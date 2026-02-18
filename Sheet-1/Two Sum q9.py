class Solution:
    def twoSum(self, nums, target):
        seen = {}
        
        for i in range(len(nums)):
            remaining = target - nums[i]
            
            if remaining in seen:
                return [seen[remaining], i]
            
            seen[nums[i]] = i
