input_array = []
total_joltage = 0

def max_subsequence(nums):
    n = len(nums)
    result = []
    start_idx = 0
    
    for _ in range(12):
        # How many more digits needed after this position
        remaining_needed = 12 - len(result)
        # Latest index to pick from (exclusive)
        end_idx = n - remaining_needed + 1
        
        # Find max in valid range
        best_idx = start_idx
        for i in range(start_idx, end_idx):
            if nums[i] > nums[best_idx]:
                best_idx = i
        
        result.append(nums[best_idx])
        start_idx = best_idx + 1
    
    return result

with open('day3_input.md', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        input_array.append([int(d) for d in line])

for i in range(len(input_array)):
    bank = input_array[i]
    print(bank)
    largest_subsequence = max_subsequence(bank)
    print(largest_subsequence)
    largest_bank_integers = int("".join(map(str, largest_subsequence)))
    print(largest_bank_integers)
    total_joltage += largest_bank_integers
    
print(total_joltage)