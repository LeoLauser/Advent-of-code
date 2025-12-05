def get_fresh_ids_in_range(IdRanges):

    fresh_ids = set()  # Using a set to avoid duplicates
    for r in IdRanges:
        start, end = map(int, r.split('-')) 
        fresh_ids.update(range(start, end + 1)) 
    return fresh_ids


if __name__ == "__main__":
    IdRanges = "Tür5/Input5.txt"  

    with open(IdRanges, 'r') as file:
        Ranges = [line.strip() for line in file if line.strip()]  # Remove empty lines

    fresh_ids = get_fresh_ids_in_range(Ranges)

    print(len(fresh_ids))
