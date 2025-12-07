filename = "Tür7/Input7.txt" 

def solve(grid):
    H = len(grid)
    W = len(grid[0])

    # Find start S
    for r in range(H):
        if "S" in grid[r]:
            c = grid[r].index("S")
            start = (r + 1, c)  # beam starts 1 row below S going downward
            break

    visited = set()     # stores ((r, c)) so a beam does not re-enter the same cell
    split_count = 0

    def trace(r, c): #you can define funktion inside function to access variables???? wild
        nonlocal split_count

        if not (0 <= r < H and 0 <= c < W): # out of range
            return

        if (r, c) in visited: #check if already visited
            return
        visited.add((r, c))

        cell = grid[r][c]

        if cell in ("."): #if space empty continue down
            trace(r + 1, c)

        elif cell == "^":# split tachyon beam
            split_count += 1
            trace(r, c - 1)
            trace(r, c + 1)

    trace(*start)
    return split_count



def read_file(filename):
    total = 0
    with open(filename) as f:
        grid = [line.rstrip("\n") for line in f]

    return grid


if __name__ == "__main__":
    print(solve(read_file(filename)))