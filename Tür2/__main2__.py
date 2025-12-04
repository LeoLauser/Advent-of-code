filename = "Input2.txt" 

def doubled(n):
    s = len(n)
    for i in range(1, s//2 + 1):
        if s % i == 0 and n == n[:i] * (s//i):
            return True
    return False


def sum_ids(filename: str) -> int:
    total = 0
    with open(filename, "r") as f:
        line = f.read().strip()

    for part in line.split(','):
        if not part:
            continue
        start, end = map(int, part.split('-'))
        for n in range(start, end + 1):
            
            if doubled(str(n)):
                total += n

    return total


if __name__ == "__main__":
    print(sum_ids(filename))