input_file = "Tür3/Input3.txt"
def max_two_digit_from_bank(bank: str) -> int:
    digits = bank.strip()
    best = -1
    
    # Compare every ordered pair
    for i in range(len(digits) - 1):
        for j in range(i + 1, len(digits)):
            num = int(digits[i] + digits[j])
            if num > best:
                best = num

    return best


def solve(filename: str) -> int:
    total = 0
    with open(filename) as f:
        for line in f:
            if line.strip():  # skip blank lines
                total += max_two_digit_from_bank(line)
    return total


if __name__ == "__main__":
    result = solve(input_file)
    print("Total output joltage:", result)
