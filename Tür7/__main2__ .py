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
    split_universe = 0
    memo = {}  #memorize recursion braches

    def trace_universe(r, c): #you can define funktion inside function to access variables???? wild
        nonlocal split_universe

        if not (0 <= r < H and 0 <= c < W): # out of range
            return 1
        
        # Memoization hit
        if (r, c) in memo:
            return memo[(r, c)]
        
        visited.add((r, c))
        cell = grid[r][c]

        if cell in ("."): #if space empty continue down
            res = trace_universe(r + 1, c)

        elif cell == "^":# split tachyon beam
            left = trace_universe(r, c - 1)
            right = trace_universe(r, c + 1)
            res = left + right # return timlines on right + left side  
        
        memo[(r, c)] = res #memorize branch result
        return res

    return trace_universe(*start)



def read_file(filename):
    total = 0
    with open(filename) as f:
        grid = [line.rstrip("\n") for line in f]

    return grid


if __name__ == "__main__":
    print(solve(read_file(filename)))