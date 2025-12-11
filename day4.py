from typing import List

rolls_of_paper = []

with open('day4_input.md', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        rolls_of_paper.append([i for i in line])

def check_left(x_cord: int, y_cord: int) -> int:
    # If there is nothing to the left, return 0
    if x_cord == 0:
        return 0
    # Add roll if there is one to the left
    if rolls_of_paper[y_cord][x_cord-1] == "@":
        return 1
    else:
        return 0

def check_right(x_cord: int, y_cord: int) -> int:
    # If there is nothing to the right, return 0
    if x_cord == len(rolls_of_paper[0])-1:
        return 0
    # Add roll if there is one to the right
    if rolls_of_paper[y_cord][x_cord+1] == "@":
        return 1
    else:
        return 0

def check_top(x_cord: int, y_cord: int) -> int:
    # If there is nothing above it, return 0
    if y_cord == 0:
        return 0
    # Add roll if there is one above it
    if rolls_of_paper[y_cord-1][x_cord] == "@":
        return 1
    else:
        return 0

def check_bottom(x_cord: int, y_cord: int) -> int:
    # If there is nothing above it, return 0
    if y_cord == len(rolls_of_paper) -1:
        return 0
    # Add roll if there is one above it
    if rolls_of_paper[y_cord+1][x_cord] == "@":
        return 1
    else:
        return 0

def check_top_left(x_cord: int, y_cord: int) -> int:
    # If top row or left column return 0
    if y_cord == 0 or x_cord == 0:
        return 0
    if rolls_of_paper[y_cord-1][x_cord-1] == "@":
        return 1
    else:
        return 0

def check_top_right(x_cord: int, y_cord: int) -> int:
    if y_cord == 0 or x_cord == len(rolls_of_paper[0])-1:
        return 0
    if rolls_of_paper[y_cord-1][x_cord+1] == "@":
        return 1
    else:
        return 0

def check_bottom_left(x_cord: int, y_cord: int) -> int:
    if y_cord == len(rolls_of_paper) -1 or x_cord == 0:
        return 0
    if rolls_of_paper[y_cord+1][x_cord-1] == "@":
        return 1
    else:
        return 0

def check_bottom_right(x_cord: int, y_cord: int) -> int:
    if y_cord == len(rolls_of_paper) -1 or x_cord == len(rolls_of_paper[0])-1:
        return 0
    if rolls_of_paper[y_cord+1][x_cord+1] == "@":
        return 1
    else:
        return 0


def get_total_neighbours(x_cord: int, y_cord: int) -> int:
    return (
        check_left(x_cord, y_cord) +
        check_right(x_cord, y_cord) +
        check_top(x_cord, y_cord) +
        check_bottom(x_cord, y_cord) +
        check_top_left(x_cord, y_cord) +
        check_top_right(x_cord, y_cord) +
        check_bottom_left(x_cord, y_cord) +
        check_bottom_right(x_cord, y_cord)
    )

def get_map_of_number_of_neighbours(roll_of_papers: List[List]) -> List[List]:
    neighbours_map = []
    for row_index, roll_row in enumerate(roll_of_papers):
        neighbours_map.append([])
        for roll_index, roll in enumerate(roll_row):
            if roll == "@":
                neighbours = get_total_neighbours(x_cord=roll_index, y_cord=row_index)
                neighbours_map[row_index].append(neighbours)
            else:
                neighbours_map[row_index].append(None)
    return neighbours_map    
    
def can_access_rolls_number(map_of_neighbours: List[List]) -> int:
    access_sum = 0
    for row in map_of_neighbours:
        for digit in row:
            if digit is None:
                continue
            elif digit < 4:
                access_sum += 1
    return access_sum

def mark_rolls_to_remove(map_of_neighbours: List[List]) -> List[List]:
    return [
        [True if cell is not None and cell < 4 else False for cell in row]
        for row in map_of_neighbours
        ]

def remove_rolls(rolls_of_paper: List[List], mask: List[List[bool]]) -> List[List]:
    return [
        [cell if not should_remove else "." for cell, should_remove in zip(row, mask_row)]
        for row, mask_row in zip(rolls_of_paper, mask)
    ]

def change_state() -> None:
    global rolls_of_paper
    accessible_roll_sum = 0
    can_access_any = True

    while can_access_any:
        map_of_neighours = get_map_of_number_of_neighbours(rolls_of_paper) 
        mask = mark_rolls_to_remove(map_of_neighours)
        if can_access_rolls_number(map_of_neighours) == 0:
            can_access_any = False
        else:
            accessible_roll_sum += can_access_rolls_number(map_of_neighours)
        rolls_of_paper = remove_rolls(rolls_of_paper, mask)
        print(rolls_of_paper)
        print(accessible_roll_sum)

print(rolls_of_paper)
change_state()