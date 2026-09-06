class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        stack=[]

        for i in range(len(temperatures)):
            temp=temperatures[i]
            while stack and temperatures[stack[-1]]<temp:
                ele_index=stack.pop()
                output[ele_index]=i-ele_index
                
            stack.append(i)
        return output



