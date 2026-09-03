class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}

        for i in strs:
            key = ''.join(sorted(i))
            
            if key in d:
                d[key].append(i)
            else:
                d[key] = [i]
        
        return list(d.values())
