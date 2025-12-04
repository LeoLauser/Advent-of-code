filename = "Input2.txt" 

def doubled(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]


def sum_ids(filename: str) -> int:
    total = 0
    with open(filename, "r") as f:
        line = f.read().strip()

    for part in line.split(','):
        if not part:
            continue
        start, end = map(int, part.split('-'))
        for n in range(start, end + 1):
            
            if doubled(n):
                total += n

    return total


if __name__ == "__main__":
    print(sum_ids(filename))