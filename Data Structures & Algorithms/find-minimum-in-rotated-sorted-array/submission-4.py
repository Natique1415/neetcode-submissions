class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minElement = 1001

        while l <= r:
            if nums[l] <= nums[r]:
                minElement = min(nums[l], minElement)
                break

            middle = (l + r) // 2

            # in left sorted half
            if nums[l] <= nums[middle]:
                l = middle + 1

            # in right sorted half
            else:
                minElement = min(nums[middle], minElement)
                r = middle - 1 

        return minElement
