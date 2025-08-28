class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):

                # we initialize the sum of all cells under consideration and the count of closest cells.
                total = count = 0
                for closestRow in range(row-1, row+2):
                    for closestCol in range(col-1, col+2):
                        if 0 <= closestRow < rows and 0 <= closestCol < cols:
                            count += 1
                            total += img[closestRow][closestCol]
                result[row][col] = total // count
        return result