class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        res = []
        n = rows + cols - 1
        for d in range(n):
            temp = []
            # row index
            row=0 if d<cols else d-cols+1
            # col index
            col = d if d<cols else cols-1

            while row < rows and col>=0:
                temp.append(mat[row][col])
                row+=1
                col-=1
            if d%2==0:
                temp = temp[::-1]

            res.extend(temp)
        return res
        