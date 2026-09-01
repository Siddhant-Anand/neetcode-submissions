class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for i in range(len(s)):
            cs=s[i]
            ct=t[i]
            d[cs]=d.setdefault(cs,0)+1
            d[ct]=d.setdefault(ct,0)-1
        
        for i in list(d.values()):
            if i<0:
                return False
        return True
