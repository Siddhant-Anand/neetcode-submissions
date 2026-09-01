class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.index=[]
        for m in range(len(matrix)):
            curr=0
            sub_index=[]
            for n in range(len(matrix[m])):
                curr+=matrix[m][n]
                sub_index.append(curr)
            self.index.append(sub_index)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=0
        for i in range(row1,row2+1):
            sl=self.index[i][col1-1] if col1>0 else 0
            sr=self.index[i][col2] 
            srow=sr-sl
            ans+=srow
        return ans



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)