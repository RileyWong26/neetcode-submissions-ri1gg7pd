class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        
        for i in range(0, len(nums)):
            # Do not reuse nums
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:
                # avoid same number numerous times
                if l > i + 1  and nums[l] == nums[l-1]:
                    l += 1
                    continue
                sum = nums[i] + nums[l] + nums[r]
                
                if sum == 0: 
                    res.append([nums[i], nums[l] , nums[r]])
                    l += 1
                # too big decrease the right pointers
                elif sum > 0:
                    r -= 1
                # Increase the left pointer
                elif sum < 0:
                    l += 1


        return res 