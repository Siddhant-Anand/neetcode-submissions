class NumArray:

    def __init__(self, nums: List[int]):
        self.index=[]
        curr=0
        for i in nums:
            curr+=i
            self.index.append(curr)
        

        

    def sumRange(self, left: int, right: int) -> int:
        sum_right=self.index[right]
        sum_left=self.index[left-1] if left >0 else 0
        return sum_right-sum_left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)