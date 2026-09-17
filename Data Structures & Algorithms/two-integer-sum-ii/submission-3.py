class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        stop=len(numbers)-1
        while start<stop:
            x=numbers[start]+numbers[stop]
            if x==target:
                return [start+1,stop+1]
            elif x<target:
                start+=1
            else:
                stop-=1
        return [-1,-1]