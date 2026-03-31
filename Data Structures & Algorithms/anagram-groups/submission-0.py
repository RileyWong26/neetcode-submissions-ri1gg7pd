class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        hashList = {}

        for string in strs:
            hashString = {"anagram": [string]}
            hash ={}
            for c in string:
                if c not in hash:
                    hash[c] = 1
                else:
                    hash[c] += 1
            
            
            # Check if an anagram already exists
            flag = False
            for hashes in hashList:
                
                if hashList[hashes]["hash"] == hash:
                    hashList[hashes]["anagram"].append(string)
                    flag = True
            if not flag:
                hashString["hash"] = hash
                hashList[string] = hashString
                
        for hash in hashList:
            output.append(hashList[hash]["anagram"])

        return output