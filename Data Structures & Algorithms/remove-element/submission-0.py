class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos_req=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                pos_req.append(i)
        n=0
        for i in pos_req:
            nums[n]=nums[i]
            n+=1
        return len(pos_req)