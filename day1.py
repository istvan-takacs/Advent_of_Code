import math

directions = [
"L68", # 1
"L30", 
"R48",
"L5",
"R60",
"L55",
"L1",
"L99",
"R14",
"L82"
]

zero_counter = 0
dial = [i for i in range(100)]

def shift_left(start_number, turn_number):
    global zero_counter
    global dial
    final_position = start_number-turn_number
    
    # Dial turns below 0
    if final_position < 1:
        # if it lands on 0
        if abs(final_position) % 100 == 0:
            zero_counter += 1
        # zeros_passed = math.ceil(abs(final_position) / 100)
        # zero_counter += zeros_passed
        final_position = (100 - ((abs(final_position)) % 100)) % 100

    return dial[final_position]

def shift_right(start_number, turn_number):
    global zero_counter
    global dial
    final_position = start_number + turn_number
    
    
    # Dial turns over 99
    if final_position > 99:
        # If lands on 0
        if final_position % 100 == 0:
            zero_counter += 1
        # zero_counter += final_position // 100
        final_position = final_position % 100

    return dial[final_position]

def turn_dial(turn, start_number=50):
    turn_direction = turn[0]
    turn_number = int(turn[1:])
    
    if turn_direction == "R":
        print(f"Turning right by {turn_number}")
        final_position = shift_right(start_number, turn_number)
    elif turn_direction == "L":
        print(f"Turning left by {turn_number}")
        final_position = shift_left(start_number, turn_number)
    print(final_position, zero_counter)
    return final_position
    
def keep_turning_dial(dial_turns_array):
    start_position = 50
    i = 0
    while i < len(dial_turns_array):
        turn = dial_turns_array[i]
        start_position = turn_dial(turn, start_position)
        i += 1



with open('day1_input.md', 'r') as f:
    lines = f.readlines()

instructions = [line.strip() for line in lines]

keep_turning_dial(instructions)