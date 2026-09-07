class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=''
        for i in s:
            if i.isalnum():
                ss+=i
        
        start=0
        stop=len(ss)-1
        ss=ss.lower()
        print(ss)

        while start<stop:
            if ss[start]!=ss[stop]:
                return False
            
            start+=1
            stop-=1
        return True
        