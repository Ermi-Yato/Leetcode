class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        num_rows, num_cols = len(img), len(img[0])
        smoothed_image = [[0] * num_cols for _ in range(num_rows)]
      
        for row in range(num_rows):
            for col in range(num_cols):
                pixel_sum = pixel_count = 0
              
                for neighbor_row in range(row - 1, row + 2):
                    for neighbor_col in range(col - 1, col + 2):
                        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                            pixel_count += 1
                            pixel_sum += img[neighbor_row][neighbor_col]
              
                smoothed_image[row][col] = pixel_sum // pixel_count
     
        return smoothed_image