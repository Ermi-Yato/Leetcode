class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            singleRow = [0] * (i+1)
            if i==0:
                output.append([1])
            elif i==1:
                output.append([1,1])
            else:
                for j in range(i+1):
                    prevRow = output[i-1]
                    if j==0 or j==i:
                        singleRow[j] = 1
                    else:
                        singleRow[j] = prevRow[j-1] + prevRow[j]
                output.append(singleRow)
        return output
        