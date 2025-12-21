from typing import List
import math
from itertools import combinations

def parse_input() -> List[List]:
    with open("day9_input.txt", "r") as file:
        l = file.read().splitlines()
        return [tuple(map(int, line.split(","))) for line in l]
    
# def get_edges(tile_locations: List[tuple]) -> List[tuple]:
#     top_row = sorted(tile_locations, key= lambda x: x[1])[0][1]
#     top_left = sorted([tile for tile in tile_locations if tile[1] == top_row], key= lambda x: x[0])[0]

#     bottom_row = sorted(tile_locations, key= lambda x: x[1], reverse=True)[0][1]
#     bottom_right = sorted([tile for tile in tile_locations if tile[1] == bottom_row], key= lambda x: x[0], reverse=True)[0]
#     return [top_left, bottom_right]

    
def get_largest_rectangle(tile_locations: List[tuple]) -> int:
    idx_tile_locations = list(enumerate(tile_locations))
    max_area = 0
    for tile in combinations(idx_tile_locations, 2):
        rectangle_x = abs(tile[0][1][0] - tile[1][1][0])+1
        rectangle_y = abs(tile[0][1][1] - tile[1][1][1])+1
        rectangle_area = rectangle_x * rectangle_y

        if rectangle_area > max_area:
            max_area = rectangle_area
        # print(tile, rectangle_area)
    return max_area

def main():
    tile_locations = parse_input()
    # print(get_edges(tile_locations))
    print(get_largest_rectangle(tile_locations))



main()