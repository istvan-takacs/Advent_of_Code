from typing import List
import re

def parse_input() -> List[List]:
    with open("day7_input.txt", "r") as f:
        diagram = [re.split(r"/*", line) for line in f.read().split()]
    return diagram

def get_upstream_possibilities(current_row_idx: int, current_char_idx: int,  diagram: List[List]) -> int:

    diagram_prev_row = diagram[current_row_idx-1]
    to_left = max(current_char_idx-1, 0)
    to_right = min(current_char_idx+1, len(diagram[current_row_idx])-1) 

    if type(diagram_prev_row[current_char_idx]) == int:
        char_above = diagram_prev_row[current_char_idx]
    else:
        char_above = 0

    if diagram[current_row_idx][current_char_idx-1] == "^" and diagram[current_row_idx][current_char_idx+1] == "^":
        upstream_possibilities = [diagram_prev_row[to_left], diagram_prev_row[to_right], char_above]
    elif diagram[current_row_idx][current_char_idx-1] == "^":
        upstream_possibilities = [diagram_prev_row[to_left], char_above]
    elif diagram[current_row_idx][current_char_idx+1] == "^":
        upstream_possibilities = [diagram_prev_row[to_right], char_above]
    else:
        upstream_possibilities = [char_above]

    return sum([possibility for possibility in upstream_possibilities if type(possibility) == int])


def parse_diagram(diagram: List[List]) -> None:

    # Draw first line below S
    beam_start_position = diagram[0].index("S")
    diagram[1][beam_start_position] = "|"


    width_of_diagram = len(diagram[0])
    last_diagram_index = len(diagram)-1
    current_row = 1
    splitting = 0
    while current_row <= last_diagram_index:
        for char_idx in range(width_of_diagram):
            # Split tacheon if there is light meets ^
            if diagram[current_row][char_idx] == "^" and diagram[current_row-1][char_idx] == "|":
                diagram[current_row][char_idx-1] = diagram[current_row][char_idx+1] = "|"
                splitting += 1
            elif diagram[current_row-1][char_idx] == "|":
                diagram[current_row][char_idx] = "|"
        current_row += 1
    print(splitting)

def traverse_splitting_probabilities(parsed_diagram: List[List]) -> int:
    beam_start_position = parsed_diagram[0].index("S")
    parsed_diagram[1][beam_start_position] = 1

    width_of_diagram = len(parsed_diagram[0])
    last_diagram_index = len(parsed_diagram)-1
    

    current_row = 2
    while current_row <= last_diagram_index:
        for char_idx in range(width_of_diagram):
            current_char = parsed_diagram[current_row][char_idx]

            if current_char == "|":
                    upstream_possibilities = get_upstream_possibilities(current_row, char_idx, parsed_diagram)
                    parsed_diagram[current_row][char_idx] = upstream_possibilities
        current_row += 1
    integers = [d for d in parsed_diagram[-1] if type(d) == int]
    print(sum(integers))
                

diagram = parse_input()
parse_diagram(diagram=diagram)
traverse_splitting_probabilities(parsed_diagram=diagram)
