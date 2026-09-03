class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}

        for i in strs:
            temp={}
            for j in i:
                temp[j]=temp.setdefault(j,0)+1

            key = tuple(sorted(temp.items()))
            
            if key in d:
                d[key].append(i)
            else:
                d[key] = [i]
        
        return list(d.values())
