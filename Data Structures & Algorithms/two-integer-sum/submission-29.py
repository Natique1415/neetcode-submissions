class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in diff_map:
                diff_map[nums[i]] = i
            else:
                return [diff_map[target - nums[i]], i] 
        