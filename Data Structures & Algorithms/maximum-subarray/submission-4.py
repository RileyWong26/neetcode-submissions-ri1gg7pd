class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -9999
        pre = 0

        for i in range(0, len(nums)):
            pre += nums[i]
            res = max(res, pre)
            if pre <= 0:
                pre = 0
    
        return res


        