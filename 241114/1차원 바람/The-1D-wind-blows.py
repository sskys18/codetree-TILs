# 변수 선언 및 입력
n, m, t = map(int, input().split())  # 행 수, 열 수, 바람이 부는 횟수
matrix = [list(map(int, input().split())) for _ in range(n)]
operations = [input().split() for _ in range(t)]

# 바람 연산 적용 함수
def shift_row(row, direction):
    if direction == 'L':
        return row[1:] + row[:1]
    elif direction == 'R':
        return row[-1:] + row[:-1]

def propagate(matrix, start_row, initial_direction, propagate_direction):
    n, m = len(matrix), len(matrix[0])
    curr_direction = initial_direction

    row = start_row
    while 0 <= row < n:
        matrix[row] = shift_row(matrix[row], curr_direction)
        next_row = row + propagate_direction

        if next_row < 0 or next_row >= n:
            break

        # Check if propagation should continue
        if any(matrix[row][col] == matrix[next_row][col] for col in range(m)):
            # Switch direction
            curr_direction = 'L' if curr_direction == 'R' else 'R'
            row = next_row
        else:
            break

# Process all wind operations
for operation in operations:
    r, d = int(operation[0]) - 1, operation[1]  # Adjust to 0-based index
    direction = 'L' if d == 'L' else 'R'

    # Initial row shift
    matrix[r] = shift_row(matrix[r], direction)
    
    # Propagate up
    propagate(matrix, r - 1, 'L' if direction == 'R' else 'R', -1)
    # Propagate down
    propagate(matrix, r + 1, 'L' if direction == 'R' else 'R', 1)

# 출력
for row in matrix:
    print(" ".join(map(str, row)))