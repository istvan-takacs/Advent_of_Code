from typing import List, Dict
import math
from itertools import combinations

def parse_input() -> List[List]:
    with open("day8_input.txt", "r") as file:
        l = file.read().splitlines()
        return [list(map(int, line.split(","))) for line in l]

def get_distance(box_one_location: List[int], box_two_location: List[int]) -> float:
    points = [(coord_one-coord_two)**2 for coord_one, coord_two in zip(box_one_location, box_two_location)]
    return math.sqrt(sum(points))

def box_distances(boxes: List[List]) -> List[List]:
    all_distances = {}
    indexed_boxes = list(enumerate(boxes))
    for pair in combinations(indexed_boxes, 2):
        idx = (pair[0][0], pair[1][0])
        all_distances[idx] = get_distance(pair[0][1], pair[1][1])
    return sorted(all_distances.items(), key=lambda x: x[1])


def find(parent: Dict[int, int], x: int) -> int:
    while parent[x] != x:
        x = parent[x]
    return x

def union(parent: Dict[int, int], x: int, y: int) -> bool:
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False

def main():
    data_boxes = parse_input()

    box_index_distances = box_distances(data_boxes)
    parent = {i: i for i in range(len(data_boxes))}

    merges = []
    for box_distance in box_index_distances[:]:
        if union(parent, box_distance[0][0], box_distance[0][1]):
            merges.append((box_distance[0][0], box_distance[0][1]))

    last_merge = merges[-1]
    print(last_merge)
    box_a_idx = last_merge[0]
    box_b_idx = last_merge[1]

    x_cord_box_a = data_boxes[box_a_idx][0]
    x_cord_box_b = data_boxes[box_b_idx][0]

    print(x_cord_box_a*x_cord_box_b)


    circuit_sizes = {}
    for i in range(len(data_boxes)):
        root = find(parent, i)
        if root in circuit_sizes:
            circuit_sizes[root] += 1
        else:
            circuit_sizes[root] = 1


    sizes = sorted(circuit_sizes.values(), reverse=True)
    print(f"Number of boxes: {len(data_boxes)}")
    print(f"Number of pairs: {len(box_index_distances)}")

    result = sizes
    print(result)



    # print(parent)
 

main()