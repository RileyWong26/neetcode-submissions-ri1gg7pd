class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        hash = {}
        occurance = 0

        # Hash with # of occurances
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
                occurance = max(occurance, hash[num])
        
    
        bucket = [[] for i in range(occurance+1)]
        for key in hash.keys():
            bucket[hash[key] - 1].append(key)
        
        for i in range(len(bucket) -1, -1, -1):
            if len(res) == k:
                return res
            for num in bucket[i]:
                res.append(num)


        return res
            
