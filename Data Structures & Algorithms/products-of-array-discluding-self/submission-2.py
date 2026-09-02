class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero=0
        curr=1
        pos=len(nums)+1
        index=[]
        for i in range(len(nums)):
            if nums[i]==0:
                count_zero+=1
                pos=min(i,pos)
            else:
                curr*=nums[i]
                index.append(curr)
        
        if count_zero==1:
            ans=[]
            for i in range(len(nums)):
                if i==pos:
                    ans.append(curr)
                else:
                    ans.append(0)
            return ans
        elif count_zero>1:
            return [0]*(len(nums))
        else:
            ans=[]
            for i in range(len(index)):
                ans.append(int(index[-1]/nums[i]))
            return ans
