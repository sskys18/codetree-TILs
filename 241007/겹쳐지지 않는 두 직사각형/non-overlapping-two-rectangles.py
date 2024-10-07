def calculate_sum(prefix, x1, y1, x2, y2):
    """ 주어진 좌표 범위 (x1, y1)에서 (x2, y2)까지의 부분합 계산 """
    total = prefix[x2+1][y2+1]
    if x1 > 0:
        total -= prefix[x1][y2+1]
    if y1 > 0:
        total -= prefix[x2+1][y1]
    if x1 > 0 and y1 > 0:
        total += prefix[x1][y1]
    return total

def max_two_rectangles_sum(n, m, grid):
    # 2D prefix sum을 계산
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(m):
            prefix[i+1][j+1] = grid[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]
    
    max_sum = float('-inf')
    
    # 가능한 모든 직사각형을 탐색
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    # 첫 번째 직사각형의 합을 계산
                    sum1 = calculate_sum(prefix, x1, y1, x2, y2)
                    
                    # 나머지 영역에서 두 번째 직사각형을 잡음
                    # 두 번째 직사각형이 첫 번째와 겹치지 않게 하기 위해서 탐색 범위를 조정
                    for x3 in range(n):
                        for y3 in range(m):
                            for x4 in range(x3, n):
                                for y4 in range(y3, m):
                                    if x4 < x1 or x3 > x2 or y4 < y1 or y3 > y2:
                                        sum2 = calculate_sum(prefix, x3, y3, x4, y4)
                                        max_sum = max(max_sum, sum1 + sum2)
    
    return max_sum

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(max_two_rectangles_sum(n, m, grid))