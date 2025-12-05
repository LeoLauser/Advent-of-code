lines, _ = open("Tür5/part2.txt").read().split("\n\n")
 
ranges = []
for line in lines.splitlines():
    start, end = map(int, line.split('-'))
    ranges.append((start, end))
 
# Sort ranges by start value
ranges.sort()
 
# Merge overlapping ranges
merged = []
for start, end in ranges:
    if not merged:
        merged.append((start, end))
    else:
        last_start, last_end = merged[-1]
        # If current range overlaps or is adjacent to the last merged range
        if start <= last_end + 1:
            # Merge: extend the last range if needed
            merged[-1] = (last_start, max(last_end, end))
        else:
            # No overlap: add as new range
            merged.append((start, end))
 
# Calculate total number of IDs in all merged ranges
total = 0
for start, end in merged:
    total += (end - start + 1)
 
print (total)