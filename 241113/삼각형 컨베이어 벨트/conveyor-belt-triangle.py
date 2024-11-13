def shift_row(row, direction):
    # 주어진 방향에 따라 행을 한 칸 이동시키는 함수
    if direction == 'L':
        return row[1:] + row[:1]
    elif direction == 'R':
        return row[-1:] + row[:-1]

def propagate(matrix, start_row, initial_direction, propagate_direction):
    # 전파 함수: 전파는 처음 방향의 반대 방향으로 계속 번져 나감
    n, m = len(matrix), len(matrix[0])
    curr_direction = initial_direction

    row = start_row
    while 0 <= row < n:
        matrix[row] = shift_row(matrix[row], curr_direction)
        next_row = row + propagate_direction

        if next_row < 0 or next_row >= n:
            break

        # 같은 열에 일치하는 숫자가 있는지 확인하여 전파 여부 결정
        if any(matrix[row][col] == matrix[next_row][col] for col in range(m)):
            # 방향을 반대로 변경
            curr_direction = 'L' if curr_direction == 'R' else 'R'
            row = next_row
        else:
            break

def process_wind(matrix, operations):
    # 각 바람에 대해 초기 행을 이동시키고 전파 처리
    for (r, d) in operations:
        r -= 1  # 0-기반 인덱스로 조정
        direction = 'L' if d == 'L' else 'R'

        # 초기 행 이동
        matrix[r] = shift_row(matrix[r], direction)
        
        # 위로 전파
        propagate(matrix, r - 1, 'L' if direction == 'R' else 'R', -1)
        # 아래로 전파
        propagate(matrix, r + 1, 'L' if direction == 'R' else 'R', 1)

def print_matrix(matrix):
    # 행렬 출력 함수
    for row in matrix:
        print(" ".join(map(str, row)))

# 입력 예시 테스트
n, m, q = 6, 5, 1
matrix = [
    [1, 5, 6, 7, 3],
    [5, 3, 2, 5, 4],
    [6, 4, 5, 2, 5],
    [2, 6, 1, 0, 5],
    [5, 1, 2, 1, 6],
    [4, 2, 5, 2, 8]
]
operations = [(3, 'L')]

# 바람을 처리하고 최종 행렬 출력
process_wind(matrix, operations)
print_matrix(matrix)