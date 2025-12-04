filename = "Tür4/Input4.txt"
def count_accessible(filename):
    # Load the grid
    with open(filename) as f:
        grid = [list(line.rstrip("\n")) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    # Directions for 8 neighbors
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            # Count neighbors that are '@'
            adjacent = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        adjacent += 1

            # Accessible if fewer than 4 '@' neighbors
            if adjacent < 4:
                accessible += 1

    return accessible


if __name__ == "__main__":
    print(count_accessible(filename))
