# This code finds the tetrahedron with the smallest volume given a set of points in 3D space,
# such that the sum of a property (stored in the 4th column) of its vertices equals 100.
# 
# Intuition:
# 1. Read points from a file.
# 2. Precompute pairwise differences of points' coordinates.
# 3. Find all pairs of points whose property sum is <= 100 and store them.
# 4. Iterate through pairs and check combinations to find tetrahedrons whose property sum equals 100.
# 5. Compute the volume of each valid tetrahedron and track the one with the smallest volume.
#
# Time Complexity: O(n^4), where n is the number of points.
# Space Complexity: O(n^2), for storing pairwise differences and pair sums.

import numpy as np
from collections import defaultdict

# Modified provided code for volume to instead calculate through only the considered
# point combinations and abstracted the actual volume calculation to add a slight optimization.
def volume_of_tetrahedron(AB, AC, AD):
    # Calculate the volume of a tetrahedron given vectors AB, AC, and AD
    volume = abs(np.dot(np.cross(AB, AC), AD)) / 6.0
    return volume

def read_points(filename):
    # Read points from a file and store them in a list
    points = []
    with open(filename, 'r') as file:
        for line in file:
            # Parse each line to extract x, y, z coordinates and the property value n
            x, y, z, n = map(float, line.strip('()\n').split(', '))
            points.append([x, y, z, int(n)])
    # Return the points as a numpy array
    return np.array(points)

def precompute_differences(points):
    # Precompute the differences between every pair of points' coordinates
    n = len(points)
    differences = np.zeros((n, n, 3))
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the difference vector from point i to point j
            differences[i, j] = points[j, :3] - points[i, :3]
            differences[j, i] = -differences[i, j]
    # Return the precomputed differences
    return differences

def find_valid_tetrahedron(points):
    n = len(points)
    points_sum = points[:, 3]
    pair_sums = defaultdict(list)
    differences = precompute_differences(points)

    # Calculate all pairs of points and their property sums
    for i in range(n):
        for j in range(i + 1, n):
            pair_sum = points_sum[i] + points_sum[j]
            if pair_sum <= 100:
                # Store pairs of points whose property sum is <= 100
                pair_sums[pair_sum].append((i, j))

    min_volume = float('inf')
    best_indices = None
    checked_combinations = set()

    # Iterate over pairs and check for valid tetrahedron combinations
    for pair_sum, pairs in pair_sums.items():
        needed_sum = 100 - pair_sum
        if needed_sum in pair_sums:
            for (i, j) in pairs:
                for (k, l) in pair_sums[needed_sum]:
                    # Form a sorted tuple of indices to ensure unique combinations
                    indices = tuple(sorted([i, j, k, l]))
                    if len(set(indices)) == 4 and indices not in checked_combinations:
                        checked_combinations.add(indices)
                        # Verify if the sum of properties equals 100
                        if points_sum[i] + points_sum[j] + points_sum[k] + points_sum[l] == 100:
                            # Compute the volume of the tetrahedron
                            AB = differences[i, j]
                            AC = differences[i, k]
                            AD = differences[i, l]
                            volume = volume_of_tetrahedron(AB, AC, AD)
                            # Track the smallest volume found
                            if volume < min_volume:
                                min_volume = volume
                                best_indices = indices
                                # Early termination if minimal volume is found
                                if min_volume == 0:
                                    return sorted(best_indices)

    return sorted(best_indices) if best_indices else None

def process_file(filename):
    # Read points from the file
    points = read_points(filename)
    # Find the tetrahedron with the smallest volume whose property sum equals 100
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
