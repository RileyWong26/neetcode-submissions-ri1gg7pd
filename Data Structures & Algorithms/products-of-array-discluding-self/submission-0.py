class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 0
        
        prefix = [0]* len(nums)
        postfix = [0] * len(nums)

        # Prefix
        prefix[1] = nums[0]
        for i in range(2 ,len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Post fix
        postfix[-2] = nums[-1]
        for i in range(len(nums) - 3, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        print(prefix, postfix)
        # output
        out = []
        for i in range(len(prefix)):            
            out.append(prefix[i] * postfix[i])
        #edges
        out[0] = postfix[0]
        out[-1] = prefix[-1]
        return out
        
