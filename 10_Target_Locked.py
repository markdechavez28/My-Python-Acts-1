def modify_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    closest_value = float('inf')
    closest_position = (-1, -1)

    for r in range(rows):
        for c in range(cols):
            diff = abs(matrix[r][c] - target)
            if diff < closest_value:
                closest_value = diff
                closest_position = (r, c)

    if closest_position == (-1, -1):
        return matrix

    target_row, target_col = closest_position

    matrix[target_row][target_col] = 0

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in directions:
        nr, nc = target_row + dr, target_col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            matrix[nr][nc] = matrix[nr][nc] // 2 

    return matrix

def main():
    dimensions = input("Row and Column Count: ").strip()
    rows, cols = map(int, dimensions)

    print(f"Enter {rows}x{cols} matrix:")
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().strip()))
        matrix.append(row)

    target = int(input("Select Target: "))

    updated_matrix = modify_matrix(matrix, target)

    for row in updated_matrix:
        print("\t".join(map(str, row)))


if __name__ == "__main__":
    main()