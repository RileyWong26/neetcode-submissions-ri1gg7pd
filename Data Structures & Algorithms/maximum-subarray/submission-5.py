class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        largest = 0

        for n in nums:
            largest += n
            res = max(res, largest)

            if largest <= 0:
                largest = 0
        
        return res