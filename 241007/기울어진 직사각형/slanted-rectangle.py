def max_skewed_rectangle_sum(n, grid):
    max_sum = 0

    # 가능한 모든 시작 지점을 탐색
    for x1 in range(n):
        for y1 in range(n):
            # 각 지점에서 가능한 모든 기울어진 직사각형을 그려봄
            for size1 in range(1, min(n - x1, y1 + 1)):  # 왼쪽 위->오른쪽 위 이동 가능한 거리
                for size2 in range(1, min(n - x1 - size1, n - y1)):  # 오른쪽 위->오른쪽 아래 이동 가능한 거리
                    # 각 기울어진 직사각형이 범위 내에 있는지 확인
                    if (x1 - size1 >= 0 and y1 + size1 < n and
                        x1 - size1 + size2 < n and y1 + size1 + size2 < n and
                        x1 + size2 < n and y1 + size2 >= 0):
                        
                        # 직사각형의 각 경로에 있는 값을 더하기
                        temp_sum = 0
                        x, y = x1, y1
                        
                        # 왼쪽 위 -> 오른쪽 위 (좌상 -> 우상)
                        for _ in range(size1):
                            x -= 1
                            y += 1
                            temp_sum += grid[x][y]
                        
                        # 오른쪽 위 -> 오른쪽 아래 (우상 -> 우하)
                        for _ in range(size2):
                            x += 1
                            y += 1
                            temp_sum += grid[x][y]
                        
                        # 오른쪽 아래 -> 왼쪽 아래 (우하 -> 좌하)
                        for _ in range(size1):
                            x += 1
                            y -= 1
                            temp_sum += grid[x][y]
                        
                        # 왼쪽 아래 -> 왼쪽 위 (좌하 -> 좌상)
                        for _ in range(size2):
                            x -= 1
                            y -= 1
                            temp_sum += grid[x][y]
                        
                        # 최댓값 갱신
                        max_sum = max(max_sum, temp_sum + grid[x1][y1])
    
    return max_sum


# 입력 처리
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 최대 합을 구해서 출력
print(max_skewed_rectangle_sum(n, grid))