class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pre, suf = [0 for i in range(N)], [0 for i in range(N)]
        
        pre[0] = nums[0]
        suf[-1] = nums[-1]

        for i in range(1, N):
            pre[i] = pre[i - 1] * nums[i]
            suf[N - i - 1] = suf[N-i] * nums[N-i-1]

        nums[0] = suf[1]
        nums[-1] = pre[-2]
        for i in range(1, N-1):
            nums[i] = pre[i-1] * suf[i+1] 

        return nums          