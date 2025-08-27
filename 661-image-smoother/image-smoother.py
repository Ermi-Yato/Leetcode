class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        out = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                total = 0
                cnt = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        rr, cc = r + dr, c + dc
                        if 0 <= rr < m and 0 <= cc < n:
                            total += img[rr][cc]
                            cnt += 1
                out[r][c] = total // cnt  # floor average
        return out