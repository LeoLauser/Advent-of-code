def load_data(filename: str):
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]


    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    sep_cols = set()
    for c in range(width):
        if all(row[c] == " " for row in grid):
            sep_cols.add(c)

    problems = []
    c = 0
    while c < width:
        if c in sep_cols:
            c += 1
            continue
        start = c
        while c < width and c not in sep_cols:
            c += 1
        end = c  # open interval
        problems.append((start, end))

    total = 0
    

    
    for start, end in problems:
        # Extract the vertical slice
        block = [row[start:end] for row in grid]

        # Bottom row includes operator;
        bottom = block[-1]
        op = None
        op_col = None
        for i, ch in enumerate(bottom):
            if ch in "+*":
                op = ch
                op_col = i
                break
        if op is None:
            raise ValueError("No operator found in block")

        # Extract numbers above operator
        nums = []
        for row in block[:-1]:  
            chunk = row.strip()
            if chunk:
                nums.append(int(chunk))

        # Compute the result of this problem
        if op == "+":
            val = sum(nums)
        else:  # op == "*"
            val = 1
            for n in nums:
                val *= n

        total += val

    print("total:", total)

def solve_part2(filename: str):
    # Read and pad lines
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    height = len(lines)
    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    # Identify separator columns (all spaces)
    sep = [all(grid[r][c] == " " for r in range(height)) for c in range(width)]

    problems = []
    c = 0
    while c < width:
        if sep[c]:
            c += 1
            continue
        start = c
        while c < width and not sep[c]:
            c += 1
        end = c
        problems.append((start, end))

    problems = problems[::-1]

    grand_total = 0

    for (start, end) in problems:
        # Operator is in the bottom row of this column block
        bottom_row = grid[-1][start:end]

        op = None
        for i, ch in enumerate(bottom_row):
            if ch in "+*":
                op = ch
                op_col = start + i
                break
        if op is None:
            raise ValueError("Operator not found")

        
        numbers = []
        for c in range(start, end):
           
            digits = []
            for r in range(height - 1):    
                ch = grid[r][c]
                if ch.strip():             
                    digits.append(ch)
            if digits:
                num = int("".join(digits))
                numbers.append(num)

        if op == "+":
            val = sum(numbers)
        else:
            val = 1
            for n in numbers:
                val *= n

        grand_total += val

    print("total2:", grand_total)

if __name__ == "__main__":
    load_data("Tür6/Input6.txt")
    solve_part2("Tür6/Input6.txt")
