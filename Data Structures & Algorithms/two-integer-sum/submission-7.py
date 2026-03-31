class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {

        }

        for i,num in enumerate(nums):
            if num in hash:
                hash[num].append(i)
            else:
                hash[num] = [i]

        for num in nums:
            diff = target - num
            if diff in hash:
                if diff == num and len(hash[num]) > 1:
                    return [hash[num][0], hash[diff][1]]
                elif diff != num:
                    return [hash[num][0], hash[diff][0]]

        return []