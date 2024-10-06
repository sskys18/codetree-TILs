# 블럭 모양 정의
blocks = [
    [(0, 0), (1, 0), (1, 1)],  # ㄱ자 모양
    [(0, 0), (0, 1), (0, 2)],  # ㅡ자 모양
]

def max_block_sum(n, m, grid):
    max_sum = 0

    # 회전 및 뒤집기 적용한 모든 블럭 정의
    all_blocks = []

    # 각 블럭을 회전하거나 뒤집은 경우의 모양을 모두 저장
    for block in blocks:
        for _ in range(4):  # 4방향 회전
            rotated_block = [(y, -x) for x, y in block]
            all_blocks.append(rotated_block)
            block = rotated_block  # 다음 회전 위한 준비

        # 뒤집기
        flipped_block = [(-x, y) for x, y in block]
        all_blocks.append(flipped_block)

    # 블럭을 모든 위치에 놓아본다
    for i in range(n):
        for j in range(m):
            for block in all_blocks:
                block_sum = 0
                valid = True
                for dx, dy in block:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m:
                        block_sum += grid[x][y]
                    else:
                        valid = False
                        break
                if valid:
                    max_sum = max(max_sum, block_sum)

    return max_sum

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(max_block_sum(n, m, grid))