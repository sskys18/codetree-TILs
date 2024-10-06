def is_happy_sequence(seq, m):
    # m이 1이면 모든 수열이 행복한 수열
    if m == 1:
        return True
    
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            count += 1
            if count >= m:
                return True
        else:
            count = 1
    return False

def count_happy_sequences(n, m, grid):
    happy_count = 0

    # 각 행에서 행복한 수열 찾기
    for row in grid:
        if is_happy_sequence(row, m):
            happy_count += 1

    # 각 열에서 행복한 수열 찾기
    for col in range(n):
        col_sequence = [grid[row][col] for row in range(n)]
        if is_happy_sequence(col_sequence, m):
            happy_count += 1

    return happy_count

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(count_happy_sequences(n, m, grid))