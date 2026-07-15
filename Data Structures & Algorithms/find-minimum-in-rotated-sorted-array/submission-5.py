class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = 1001

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            middle = (l + r) // 2
            res = min(res,nums[middle])

            if nums[l] <= nums[middle]:
                l = middle + 1 

            else:
                r = middle - 1 

        return res
