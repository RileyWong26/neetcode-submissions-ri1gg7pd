class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            res = min(res, nums[mid])

            # Check right subarray
            if nums[r] <= nums[mid]:
                l = mid + 1

            # Check left subarray
            else:
                r = mid - 1

        return res
