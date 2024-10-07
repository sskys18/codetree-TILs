def max_positive_rectangle(n, m, grid):
    max_area = -1  # 최대 크기의 직사각형의 넓이, 없다면 -1을 반환
    
    # 가능한 모든 직사각형을 탐색
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    # 직사각형이 모두 양수인지 확인
                    all_positive = True
                    for i in range(x1, x2 + 1):
                        for j in range(y1, y2 + 1):
                            if grid[i][j] <= 0:
                                all_positive = False
                                break
                        if not all_positive:
                            break
                    if all_positive:
                        # 직사각형 크기 계산
                        area = (x2 - x1 + 1) * (y2 - y1 + 1)
                        max_area = max(max_area, area)
    
    return max_area

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 최대 크기의 양수 직사각형 구하기
print(max_positive_rectangle(n, m, grid))