class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index=[]
        cur=0
        for i in nums:
            cur+=i
            index.append(cur)
        
        for i in range(len(index)):
            element=nums[i]
            sl=index[i-1] if i>0 else 0
            sr=index[-1] -index[i]
            if sl==sr:
                return i
        return -1