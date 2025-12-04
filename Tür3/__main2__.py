input_file = "Tür3/Input3.txt"

def best_subsequence_of_length(bank, k):
    bank = bank.strip()
    n = len(bank)
    result = []
    start = 0  # where we can start looking for the next digit

    for pick in range(k):
        # We must leave room for the remaining picks:
        max_start = n - (k - pick)
        
        # Choose the largest digit between start..max_start
        best_digit = '0'
        best_index = start
        
        for i in range(start, max_start + 1):
            if bank[i] > best_digit:
                best_digit = bank[i]
                best_index = i
                # If we find '9', that's optimal; cannot do better
                if best_digit == '9':
                    break
        
        result.append(best_digit)
        start = best_index + 1  # move past chosen digit

    return "".join(result)


def solve(filename: str, k: int = 12) -> int:
    total = 0
    with open(filename) as f:
        for line in f:
            if line.strip():
                best = best_subsequence_of_length(line, k)
                total += int(best)
    return total


if __name__ == "__main__":
    result = solve(input_file)
    print("Total output joltage:", result)
