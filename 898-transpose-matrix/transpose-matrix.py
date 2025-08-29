class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        # fill the transposed matrix with zero
        transposedMatrix = [[0]*rows for _ in range(cols)]

        # use the transposed matrix dimensions
        for row in range(len(transposedMatrix)):
            for col in range(len(transposedMatrix[0])):
                transposedMatrix[row][col] = matrix[col][row]

        return transposedMatrix
        