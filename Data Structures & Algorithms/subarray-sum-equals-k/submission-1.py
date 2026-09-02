class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        index=[]
        cur=0
        for i in nums:
            cur+=i
            index.append(cur)
        
        cur=0
        r_index=[]
        for i in range(len(nums)-1,-1,-1):
            cur+=nums[i]
            r_index.append(cur)
        
        d={0:1}
        ans=0

        for i in range(len(nums)):
            rem=index[i]-k
            if rem in d:
                ans+=d.get(rem)
            d[index[i]]=d.setdefault(index[i],0)+1

        
        return ans