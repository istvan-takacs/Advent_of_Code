with open("day5_input.md", "r") as f:
    lines = f.read().splitlines()

fresh_ranges = [line for line in lines if "-" in line]
item_ids = list(map(int, [line for line in lines if "-"  not in line and line != ""]))


fresh_intervals = [list(map(int,fresh_range.split("-"))) for fresh_range in fresh_ranges]

# fresh_count = 0
# for item in item_ids:
#     for range_tuple in fresh_array_tuples:
#         if item < range_tuple[0]:
#             continue
#         elif item > range_tuple[1]:
#             continue
#         else:
#             fresh_count += 1
#             break


# Sort the intervals first
fresh_intervals.sort(key=lambda x: x[0])

merged_fresh_intervals = [fresh_intervals[0]]
for interval in fresh_intervals[1:]:
    last_merged = merged_fresh_intervals[-1]

    # if the beginning of the new overlaps with the end of the old
    if interval[0] <= last_merged[1]:
        last_merged[1] = max(last_merged[1], interval[1])
    else:
        merged_fresh_intervals.append(interval)


print(fresh_intervals)
print(item_ids)
print(merged_fresh_intervals)

list_of_interval_lengths = [interval[1]-interval[0]+1 for interval in merged_fresh_intervals]
total_length = sum(list_of_interval_lengths)
print(total_length)






