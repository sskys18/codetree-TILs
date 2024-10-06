def max_coins_in_3x3_grid(N, grid):
    max_coins = 0

    # 3x3 격자를 돌 수 있는 모든 시작점을 탐색 (격자 범위 내에서)
    for i in range(N - 2):
        for j in range(N - 2):
            # 3x3 부분 격자의 동전(1)의 개수를 센다.
            current_coins = sum(grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3))
            max_coins = max(max_coins, current_coins)

    return max_coins

# 입력 받기
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(max_coins_in_3x3_grid(N, grid))