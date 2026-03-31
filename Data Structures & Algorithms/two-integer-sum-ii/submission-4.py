class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binary_search(start, end, diff):
            mid = ((end - start)// 2 ) + start
            
            # Return if found 
            if numbers[mid] == diff:
                return mid 

            if start == end:
                return -1
            
            # not found
            if numbers[mid] > diff:
                return binary_search (start, mid - 1, diff)
            return binary_search(mid+1, end, diff)
            

        for i in range (0, len(numbers)):
            # number we will look for in binary search
            diff = target - numbers[i]
            
            ans = binary_search (i+ 1, len(numbers)-1, diff)
            if ans != -1 :
                return [i + 1, ans+1]

        return [0,0]