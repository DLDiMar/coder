import numpy as np
from multiprocessing import Pool
import itertools

def calculate_volume(edge):
    """Calculate the volume of a cube given the length of its edge."""
    return edge ** 3

def process_point(point, points_array, points):
    max_volume = 0
    for p2 in points_array:
        if np.any(point[:3] != p2[:3]):
            edge = np.linalg.norm(point[:3] - p2[:3])
            p3 = (point[0], point[1], p2[2])
            p4 = (p2[0], p2[1], point[2])
            p5 = (point[0], p2[1], point[2])
            p6 = (p2[0], point[1], point[2])
            p7 = (point[0], p2[1], p2[2])
            p8 = (p2[0], point[1], p2[2])
            if (p3 in points) and (p4 in points) and (p5 in points) and (p6 in points) and (p7 in points) and (p8 in points):
                validators_sum = point[3] + p2[3] + sum(p[3] for p in points if p[:3] in [p3, p4, p5, p6, p7, p8])
                if validators_sum == 100:
                    volume = calculate_volume(edge)
                    max_volume = max(max_volume, volume)
    return max_volume

def largest_volume(file_name):
    """Find the largest volume of a hexahedron in a sea of data points with constraints."""
    points = set()
    with open(file_name, 'r') as f:
        for line in f:
            x, y, z, n = map(int, line.strip('()\n').split(','))
            points.add((x, y, z, n))

    points_array = np.array(list(points))

    with Pool() as pool:
        max_volumes = pool.starmap(process_point, [(point, points_array, points) for point in points_array])

    return max(max_volumes)

# Generate example data points
with open('points.txt', 'w') as f:
    for x, y, z in itertools.product(range(10), repeat=3):
        if x == 1 and y == 1 and z == 1:
            n = 30
        else:
            n = 10
        f.write(f'({x}, {y}, {z}, {n})\n')

print(largest_volume('points.txt'))
