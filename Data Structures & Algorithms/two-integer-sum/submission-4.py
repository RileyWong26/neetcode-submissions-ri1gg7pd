class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []

        for i, num in enumerate(nums):
            p2 = len(nums) - 1
            # Move second pointer back to the index
            while p2 > i+1 and nums[p2] + num != target:
                p2 -= 1
            if nums[p2] + num == target:
                output.append(i)
                output.append(p2)
                return output

        return output

