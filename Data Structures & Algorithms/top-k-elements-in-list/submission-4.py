class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        # Track count of all numbers in the list 
        hash = {}

        freq = [[] for i in range(len(nums) + 1)]

        for n in nums: 
            # Increase occurance count 
            hash[n] = hash.get(n,0 ) + 1
            
        for num, count in hash.items():
            freq[count].append(num)
        

        # Iterate through frequency array
        for i in range (len(freq)-1, 0, -1):
            if len(res) == k: 
                return res 

            
            while len(freq[i]) != 0:
                res.append(freq[i].pop(0))
                if len(res) == k:
                    return res
            
        return res 