class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        def sortingFunc(n: int) -> int:
            num = hash[n]
            return num

        output = []

        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        
        for key in hash:
            if len(output) == k:
                if hash[key] > hash[output[0]]:
                    output[0] = key
            
            else:
                if len(output) > 0:
                    output.append(key)

                    # Sort
                    
                else:
                    output.append(key)
            output.sort(key=sortingFunc)
        return output