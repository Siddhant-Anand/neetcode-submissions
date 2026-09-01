class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=-1
        cur=0
        for i in nums:
            if i==1:
                cur+=1
            else:
                ans=max(ans,cur)
                cur=0
        return max(ans,cur)
        