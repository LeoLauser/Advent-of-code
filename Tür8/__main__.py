import math
filename = "Tür8/Input8.txt" 

def read_file(filename):
    points = []
    with open(filename) as file:
        for line in file:
            if line.strip():
                x, y, z = map(int, line.split(","))
                points.append((x, y, z))
    return points




def solve(points):

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        parent[rb] = ra
        size[ra] += size[rb]

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    
#############################################################################################################

    parent = list(range(len(points)))
    size = [1] * len(points)

    pairs = calculate_pair_dist(points)


    for k in range(1000): # connect first 1000 closest pairs
        _, a, b = pairs[k]
        union(a, b)


    circuits = {}
    for i in range(len(points)):
        r = find(i)
        circuits[r] = circuits.get(r, 0) + 1
    sizes = sorted(circuits.values(), reverse=True)
    ans = sizes[0] * sizes[1] * sizes[2]

    return ans


def calculate_pair_dist(points): #calculate distances between all point pairs
    pairs = [] 
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            (x1, y1, z1) = points[i]
            (x2, y2, z2) = points[j]
            dist = math.dist((x1, y1, z1), (x2, y2, z2))
            pairs.append((dist, i, j))
    pairs.sort()
    return pairs# sort pairs by distance


if __name__ == "__main__":
    print(solve(read_file(filename)))