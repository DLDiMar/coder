import numpy as np
from collections import defaultdict

def volume_of_tetrahedron(AB, AC, AD):
    volume = abs(np.dot(np.cross(AB, AC), AD)) / 6.0
    return volume

def read_points(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y, z, n = map(float, line.strip('()\n').split(', '))
            points.append([x, y, z, int(n)])
    return np.array(points)

def precompute_differences(points):
    n = len(points)
    differences = np.zeros((n, n, 3))
    for i in range(n):
        for j in range(i + 1, n):
            differences[i, j] = points[j, :3] - points[i, :3]
            differences[j, i] = -differences[i, j]
    return differences

def find_valid_tetrahedron(points):
    n = len(points)
    points_sum = points[:, 3]
    pair_sums = defaultdict(list)
    differences = precompute_differences(points)

    # Calculate all pairs and their sums
    for i in range(n):
        for j in range(i + 1, n):
            pair_sum = points_sum[i] + points_sum[j]
            if pair_sum <= 100:
                pair_sums[pair_sum].append((i, j))

    min_volume = float('inf')
    best_indices = None
    checked_combinations = set()

    # Iterate over pairs and check for valid combinations
    for pair_sum, pairs in pair_sums.items():
        needed_sum = 100 - pair_sum
        if needed_sum in pair_sums:
            for (i, j) in pairs:
                for (k, l) in pair_sums[needed_sum]:
                    indices = tuple(sorted([i, j, k, l]))
                    if len(set(indices)) == 4 and indices not in checked_combinations:
                        checked_combinations.add(indices)
                        if points_sum[i] + points_sum[j] + points_sum[k] + points_sum[l] == 100:
                            AB = differences[i, j]
                            AC = differences[i, k]
                            AD = differences[i, l]
                            volume = volume_of_tetrahedron(AB, AC, AD)
                            if volume < min_volume:
                                min_volume = volume
                                best_indices = indices
                                # Early termination if minimal volume is found
                                if min_volume == 0:
                                    return sorted(best_indices)

    return sorted(best_indices) if best_indices else None

def process_file(filename):
    points = read_points(filename)
    result = find_valid_tetrahedron(points)
    if result:
        print(f"Indices of points forming the valid tetrahedron with the smallest volume in {filename}: {result}")
    else:
        print(f"No valid tetrahedron found in {filename}.")

def main():
    files = ['points_small.txt', 'points_large.txt']
    for file in files:
        process_file(file)

if __name__ == "__main__":
    main()
