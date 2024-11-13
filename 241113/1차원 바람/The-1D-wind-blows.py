def shift_row(row, direction):
    if direction == 'L':
        return row[1:] + row[:1]
    elif direction == 'R':
        return row[-1:] + row[:-1]

def propagate(matrix, start_row, direction, propagate_direction):
    n, m = len(matrix), len(matrix[0])
    curr_direction = direction

    row = start_row
    while 0 <= row < n:
        matrix[row] = shift_row(matrix[row], curr_direction)
        next_row = row + propagate_direction

        if next_row < 0 or next_row >= n:
            break

        # Check if propagation should continue
        if any(matrix[row][col] == matrix[next_row][col] for col in range(m)):
            curr_direction = 'L' if curr_direction == 'R' else 'R'
            row = next_row
        else:
            break

def process_wind(matrix, operations):
    for (r, d) in operations:
        r -= 1  # Adjusting to 0-based index
        direction = 'L' if d == 'L' else 'R'

        # Shift the initial row
        matrix[r] = shift_row(matrix[r], direction)
        
        # Propagate up and down
        propagate(matrix, r - 1, 'L' if direction == 'R' else 'R', -1)
        propagate(matrix, r + 1, 'L' if direction == 'R' else 'R', 1)

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Input parsing
n, m, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
operations = [input().split() for _ in range(q)]
operations = [(int(r), d) for r, d in operations]

# Process all wind operations
process_wind(matrix, operations)

# Output the final state of the matrix
print_matrix(matrix)